import conn as dbConn


def truncateLlTables():
    db = "./laLiga.db"
    conn = dbConn.createConnection(db)
    spSql = """DELETE FROM sportpesaLaLiga"""
    btkSql = """DELETE FROM betikaLaLiga"""
    bt22Sql = """DELETE FROM bet22LaLiga"""
    mlSql = """DELETE FROM melLaLiga"""
    x1Sql = """DELETE FROM x1betLaLiga"""
    combsSql = """DELETE FROM LLCombinations"""
    cur = conn.cursor()
    cur.execute(spSql)
    cur.execute(btkSql)
    cur.execute(bt22Sql)
    cur.execute(mlSql)
    cur.execute(combsSql)
    cur.execute(x1Sql)
    conn.commit()
    return cur.lastrowid


if __name__ == "__main__":
    truncateLlTables()
