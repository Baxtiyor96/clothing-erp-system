from flask import Flask, render_template_string

app = Flask(__name__)

HTML = '''
<!DOCTYPE html>
<html>
<head>
    <title>Clothing Company ERP</title>
    <style>
        body { font-family: Arial; margin: 0; background: #f0f2f5; }
        .header { background: #2E75B6; color: white; padding: 15px 30px; }
        .nav { background: #1F4E79; padding: 10px 30px; }
        .nav a { color: white; margin-right: 20px; text-decoration: none; }
        .container { padding: 30px; }
        .cards { display: flex; gap: 20px; margin-bottom: 30px; }
        .card { background: white; padding: 20px; border-radius: 8px; flex: 1; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }
        .card h3 { color: #2E75B6; margin: 0 0 10px 0; }
        .card .number { font-size: 36px; font-weight: bold; color: #1F4E79; }
        table { width: 100%; background: white; border-collapse: collapse; border-radius: 8px; }
        th { background: #2E75B6; color: white; padding: 12px; text-align: left; }
        td { padding: 12px; border-bottom: 1px solid #eee; }
        tr:hover { background: #f5f9ff; }
    </style>
</head>
<body>
    <div class="header">
        <h2>🏭 Clothing Company — ERP System</h2>
    </div>
    <div class="nav">
        <a href="#">Dashboard</a>
        <a href="#">Orders</a>
        <a href="#">Customers</a>
        <a href="#">Warehouse</a>
        <a href="#">Reports</a>
    </div>
    <div class="container">
        <div class="cards">
            <div class="card">
                <h3>Total Orders</h3>
                <div class="number">1,248</div>
            </div>
            <div class="card">
                <h3>Customers</h3>
                <div class="number">342</div>
            </div>
            <div class="card">
                <h3>Revenue</h3>
                <div class="number">$84,200</div>
            </div>
            <div class="card">
                <h3>Products</h3>
                <div class="number">567</div>
            </div>
        </div>
        <table>
            <tr>
                <th>Order ID</th>
                <th>Customer</th>
                <th>Product</th>
                <th>Amount</th>
                <th>Status</th>
            </tr>
            <tr><td>#1001</td><td>Toshkent Store</td><td>Winter Jacket</td><td>$1,200</td><td>✅ Delivered</td></tr>
            <tr><td>#1002</td><td>Samarqand Shop</td><td>Summer Dress</td><td>$850</td><td>🔄 Processing</td></tr>
            <tr><td>#1003</td><td>Namangan Market</td><td>Jeans Pack</td><td>$2,100</td><td>✅ Delivered</td></tr>
            <tr><td>#1004</td><td>Fergana Outlet</td><td>T-Shirts Box</td><td>$650</td><td>📦 Shipped</td></tr>
            <tr><td>#1005</td><td>Buxoro Store</td><td>Wool Sweater</td><td>$1,800</td><td>🔄 Processing</td></tr>
        </table>
    </div>
</body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(HTML)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
