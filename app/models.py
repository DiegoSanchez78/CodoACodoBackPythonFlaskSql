from app.database import get_db

class Producto:

    def __init__(self, id=None, Categoría=None, nombre_producto=None, material=None, descripcion=None, precio=None, imagen=None):   
        self.id = id
        self.categoria = Categoría
        self.nombre_producto = nombre_producto
        self.material = material
        self.descripcion = descripcion
        self.precio = precio
        self.imagen = imagen


    @staticmethod
    def get(id):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE id = %s", (id,))
        row = cursor.fetchone()
        cursor.close()
        if row:
            return Producto(id=row[0], Categoría=row[1], nombre_producto=row[2], material=row[3], descripcion=row[4], precio=row[5], imagen=row[6])
        else:
            return None
    @staticmethod
    def get_all():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos")
        rows = cursor.fetchall()
        productos = [Producto(id=row[0], Categoría=row[1], nombre_producto=row[2], material=row[3], descripcion=row[4], precio=row[5], imagen=row[6]) for row in rows]
        cursor.close()
        return productos
    
    def save(self):
        db = get_db()
        cursor = db.cursor()
        if self.id:
            cursor.execute(""" 
                UPDATE productos 
                SET Categoría=%s, nombre_producto=%s, material=%s, descripcion=%s, precio=%s, imagen=%s
                WHERE id=%s
                """, (self.categoria, self.nombre_producto, self.material, self.descripcion, self.precio, self.imagen, self.id))
        else:
            cursor.execute("""
                INSERT INTO productos (Categoría, nombre_producto, material, descripcion, precio, imagen)
                VALUES (%s, %s, %s, %s, %s, %s)
            """, (self.categoria, self.nombre_producto, self.material, self.descripcion, self.precio, self.imagen))
            self.id = cursor.lastrowid
        db.commit()
        cursor.close()

    def delete(self):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (self.id,))
        db.commit()
        cursor.close()
    
    def fetch_productos_by_categoria(categoria):
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM productos WHERE Categoria = %s", (categoria,))
        rows = cursor.fetchall()
        productos = [
        {
            'id': row[0],
            'categoria': row[1],
            'nombre_producto': row[2],
            'material': row[3],
            'descripcion': row[4],
            'precio': row[5],
            'imagen': row[6]
        }
        for row in rows
        ]
        cursor.close()
        db.close()
        return productos
    
    @staticmethod
    def get_categorias():
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SELECT DISTINCT Categoría FROM productos")
        rows = cursor.fetchall()
        categorias = [{'categoria': row[0]} for row in rows]
        cursor.close()
        return categorias
        
    def serealize(self):
        return {
            'id': self.id,
            'categoria': self.categoria,
            'nombre_producto': self.nombre_producto,
            'material': self.material,
            'descripcion': self.descripcion,
            'precio': self.precio,
            'imagen': self.imagen
        }