import pymysql

from database.connections import get_connection
from ingestion.metadata_extractor import extract_metadata
from ingestion.thumbnail import create_thumbnail

def get_or_create_telescope(cursor,telescope_name):
    if telescope_name is None:
        return None
    cursor.execute("""SELECT telescope_id FROM telescopes WHERE telescope_name=%s""",(telescope_name,))
    result=cursor.fetchone()
    if result:
        return result['telescope_id']
    cursor.execute("""INSERT INTO telescopes(telescope_name) VALUES (%s)""",(telescope_name,))
    return cursor.lastrowid



def get_or_create_instrument(cursor,instrument_name):
    if instrument_name is None:
        return None
    cursor.execute("""SELECT instrument_id FROM instruments WHERE instrument_name=%s""",(instrument_name,))
    result=cursor.fetchone()
    if result:
        return result['instrument_id']
    cursor.execute("""INSERT INTO instruments(instrument_name) VALUES(%s)""",(instrument_name,))
    return cursor.lastrowid




def get_or_create_filter(cursor,filter_name):
    if filter_name is None:
        return None
    cursor.execute("""SELECT filter_id FROM filters WHERE filter_name=%s""",(filter_name,))
    result=cursor.fetchone()
    if result:
        return result['filter_id']
    cursor.execute("""INSERT INTO filters (filter_name) VALUES (%s)""",(filter_name,))
    return cursor.lastrowid



def get_or_create_observer(cursor,observer_name):
    if observer_name is None:
        return None
    cursor.execute("""SELECT observer_id FROM observers WHERE observer_name=%s""",(observer_name,))
    result=cursor.fetchone()
    if result:
        return result['observer_id']
    cursor.execute("""INSERT INTO observers (observer_name) VALUES (%s)""",(observer_name,))
    return cursor.lastrowid




def ingest_image(file_path):
    metadata=extract_metadata(file_path)

    if metadata is None:
        print("No metadata found. Exiting.")
        return
    
    thumbnail_path=create_thumbnail(file_path)
    if thumbnail_path is None:
        print("Failed to create thumbnail. Exiting.")
        return
    conn=None
    try:
        conn=get_connection()
        cursor=conn.cursor()
        telescope_id=get_or_create_telescope(cursor,metadata["telescope"])
        instrument_id=get_or_create_instrument(cursor,metadata["instrument"])
        filter_id=get_or_create_filter(cursor,metadata["filter"])
        observer_id=get_or_create_observer(cursor,metadata["observer"])

        cursor.execute("""
    INSERT INTO images(
                object_name,
                observation_date,
                observation_time,
                telescope_id,
                instrument_id,
                observer_id,
                filter_id,
                exposure_time,
                ra,
                dec_coord,
                file_path,
                thumbnail_path,
                image_format,
                image_size_mb
                )
                VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
""",(
    metadata["object_name"],
    metadata["observation_date"],
    metadata["observation_time"],
    telescope_id,
    instrument_id,
    observer_id,
    filter_id,
    metadata["exposure_time"],
    metadata["ra"],
    metadata["dec_coord"],
    metadata["file_path"],
    thumbnail_path,
    metadata["image_format"],
    metadata["image_size_mb"]
))
        conn.commit()
        print(f"Successfully ingested image: {metadata['file_path']}")
        return True
    
    except pymysql.err.IntegrityError as e:
        if e.args[0] == 1062:
            print("Image already archived.")
            return "duplicate"

        print(f"Database error: {e}")
        return False

    except Exception as e:
        if conn:
            conn.rollback() #rollback means if there is an error, it will undo any changes made to the database during the transaction
        print(f"Error ingesting image: {e}")
        return False
    finally:
        if conn:
            conn.close()