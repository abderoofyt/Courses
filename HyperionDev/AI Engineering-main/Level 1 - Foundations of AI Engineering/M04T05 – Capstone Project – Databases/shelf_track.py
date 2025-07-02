import sqlite3

# -------------------------------------------
# ● add new books to the database,
def enter_book():
    try:
        book_id = int(input("Enter book ID (4 digits): "))
        if len(str(book_id)) != 4:
            raise ValueError("Book ID must be exactly 4 digits.")

        title = input("Enter book title: ").strip()
        if not title:
            raise ValueError("Book title cannot be empty.")

        author_id = int(input("Enter author ID (4 digits): "))
        if len(str(author_id)) != 4:
            raise ValueError("Author ID must be exactly 4 digits.")

        qty = int(input("Enter quantity: "))
        if qty < 0:
            raise ValueError("Quantity cannot be negative.")

        conn = create_connection()
        if conn is None:
            return

        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)',
                (book_id, title, author_id, qty)
            )
            print("✅ Book added successfully.")

    except ValueError as ve:
        print(f"❌ Input Error: {ve}")
    except sqlite3.IntegrityError as ie:
        print(f"❌ Database Integrity Error: {ie}")
    except sqlite3.Error as e:
        print(f"❌ Database Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

# -------------------------------------------
# ● update book information,
# ✅ Modify update_book() to also allow updating author's info
def update_book():
    try:
        book_id = int(input("Enter the ID of the book to update: "))
        conn = create_connection()
        if conn is None:
            return

        with conn:
            cursor = conn.cursor()

            # Get current book and author info using INNER JOIN
            cursor.execute('''
                SELECT book.title, author.name, author.country, author.id
                FROM book
                INNER JOIN author ON book.authorID = author.id
                WHERE book.id = ?
            ''', (book_id,))
            result = cursor.fetchone()

            if result is None:
                print("❌ Book not found.")
                return

            title, author_name, author_country, author_id = result
            print(f"\nCurrent Title: {title}")
            print(f"Current Author: {author_name}")
            print(f"Author's Country: {author_country}")

            print("\nWhat would you like to update?")
            print("1. Title\n2. Author Name\n3. Author Country\n4. Quantity")
            option = input("Choose an option: ").strip()

            if option == "1":
                new_title = input("Enter new title: ").strip()
                if not new_title:
                    raise ValueError("Title cannot be empty.")
                cursor.execute('UPDATE book SET title = ? WHERE id = ?', (new_title, book_id))
                print("✅ Title updated.")

            elif option == "2":
                new_author = input("Enter new author name: ").strip()
                if not new_author:
                    raise ValueError("Author name cannot be empty.")
                cursor.execute('UPDATE author SET name = ? WHERE id = ?', (new_author, author_id))
                print("✅ Author name updated.")

            elif option == "3":
                new_country = input("Enter author's new country: ").strip()
                if not new_country:
                    raise ValueError("Country cannot be empty.")
                cursor.execute('UPDATE author SET country = ? WHERE id = ?', (new_country, author_id))
                print("✅ Author country updated.")

            elif option == "4":
                new_qty = int(input("Enter new quantity: "))
                if new_qty < 0:
                    raise ValueError("Quantity cannot be negative.")
                cursor.execute('UPDATE book SET qty = ? WHERE id = ?', (new_qty, book_id))
                print("✅ Quantity updated.")

            else:
                print("❌ Invalid option selected.")

    except ValueError as ve:
        print(f"❌ Input Error: {ve}")
    except sqlite3.Error as e:
        print(f"❌ Database Error: {e}")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
# -------------------------------------------
# ● delete books from the database,
def delete_book():
    try:
        book_id = int(input("Enter the ID of the book to delete: "))
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute('DELETE FROM book WHERE id = ?', (book_id,))
        conn.commit()
        conn.close()
        print("✅ Book deleted successfully.")
    except ValueError:
        print("❌ Invalid input. Please enter a numeric book ID.")


# -------------------------------------------
# ● search the database to find a specific book.
def search_books():
    keyword = input("Enter title or ID to search: ")
    conn = create_connection()
    cursor = conn.cursor()
    try:
        if keyword.isdigit():
            cursor.execute('SELECT * FROM book WHERE id = ?', (int(keyword),))
        else:
            cursor.execute('SELECT * FROM book WHERE title LIKE ?', ('%' + keyword + '%',))
        
        results = cursor.fetchall()
        if results:
            print("📚 Books found:")
            for book in results:
                print(f"ID: {book[0]}, Title: {book[1]}, Author ID: {book[2]}, Qty: {book[3]}")
        else:
            print("❌ No matching books found.")
    finally:
        conn.close()



# -------------------------------------------
# Create a database called ebookstore, and a table called book.
def create_connection():
    try:
        return sqlite3.connect("ebookstore.db")
    except sqlite3.Error as e:
        print(f"❌ Database connection failed: {e}")
        return None

# -------------------------------------------
# Requirement: Create table and populate initial data
def setup_database():
    conn = create_connection()
    cursor = conn.cursor()

    # ✅ Requirement 2: Create table called book
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS book (
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            authorID INTEGER,
            qty INTEGER
        )
    ''')

    # Populate the table with values. You can also add your own values if you wish.
    # The table should have the following structure: 
    # id/title/authorID/qty
    # 3001/A Tale of Two Cities/1290/30
    # 3002/Harry Potter and the Philosopher's Stone/8937/40/
    # 3003/The Lion, the Witch and the Wardrobe/2356/25/
    # 3004/The Lord of the Rings/6380
    # /3005/Alice’s Adventures in Wonderland/5620/12
    books = [
        (3001, "A Tale of Two Cities", 1290, 30),
        (3002, "Harry Potter and the Philosopher's Stone", 8937, 40),
        (3003, "The Lion, the Witch and the Wardrobe", 2356, 25),
        (3004, "The Lord of the Rings", 6380, 37),
        (3005, "Alice’s Adventures in Wonderland", 5620, 12)
    ]

    cursor.executemany('''
        INSERT OR IGNORE INTO book (id, title, authorID, qty) VALUES (?, ?, ?, ?)
    ''', books)

    conn.commit()
    conn.close()

    # ✅ Part 2 - Step 1: Create author table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS author (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            country TEXT
        )
    ''')

    # ✅ Part 2 - Step 2: Populate the author table
    authors = [
        (1290, "Charles Dickens", "England"),
        (8937, "J.K. Rowling", "England"),
        (2356, "C.S. Lewis", "Ireland"),
        (6380, "J.R.R. Tolkien", "South Africa"),
        (5620, "Lewis Carroll", "England")
    ]

    # Avoid duplicates if run multiple times
    for author in authors:
        cursor.execute('INSERT OR IGNORE INTO author (id, name, country) VALUES (?, ?, ?)', author)

#✅ Part 2 - Step 2: Populate the author table
def view_book_details():
    conn = create_connection()
    cursor = conn.cursor()

    # ✅ INNER JOIN to fetch book title, author name and country
    cursor.execute('''
        SELECT book.title, author.name, author.country
        FROM book
        INNER JOIN author ON book.authorID = author.id
    ''')

    rows = cursor.fetchall()
    conn.close()

    print("\n📚 Details")
    print("-" * 50)
    for title, name, country in rows:
        print(f"Title: {title}")
        print(f"Author's Name: {name}")
        print(f"Author's Country: {country}")
        print("-" * 50)


# -------------------------------------------
# The program should present the user with the following menu:
def main_menu():
    setup_database()

    while True:
        print("\nMenu:")
        print("1. Enter book")
        print("2. Update book")
        print("3. Delete book")
        print("4. Search books")
        print("5. View details of all books")  # ✅ Part 2 - Step 3
        print("0. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            enter_book()
        elif choice == "2":
            update_book()
        elif choice == "3":
            delete_book()
        elif choice == "4":
            search_books()
        elif choice == "5":
            view_book_details()  # ✅ New function
        elif choice == "0":
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid selection.")

# ✅ Entry point check
if __name__ == "__main__":
    main_menu()
