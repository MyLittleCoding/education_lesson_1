# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: LearnPath
def delete_record(record_id, table_name):
    if not record_id:
        print(f"Ошибка: идентификатор '{record_id}' пуст.")
        return False
    
    try:
        conn = sqlite3.connect('learnpath.db')
        cursor = conn.cursor()
        
        query = f"""
            DELETE FROM {table_name} 
            WHERE id = ?
        """
        
        cursor.execute(query, (record_id,))
        deleted_count = cursor.rowcount
        
        if deleted_count > 0:
            print(f"Запись с ID '{record_id}' успешно удалена из таблицы '{table_name}'.")
            conn.commit()
            return True
        else:
            print(f"Запись с ID '{record_id}' не найдена в таблице '{table_name}'.")
            conn.rollback()
            return False
            
    except sqlite3.Error as e:
        print(f"Произошла ошибка при удалении записи: {e}")
        if 'conn' in locals():
            conn.rollback()
        return False
        
    finally:
        if 'conn' in locals():
            conn.close()
