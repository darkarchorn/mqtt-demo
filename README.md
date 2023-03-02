# mqtt-demo
Cài Python tại https://www.python.org/downloads/  
Chạy lần lượt các lệnh sau vào terminal:  
python -m ensurepip --default-pip  
pip install paho-mqtt  

# Note  
Trong mỗi file chúng ta có 2 dòng sau:  
client.connect(mqttBroker) -> connect tới broker của url https://mqtt.eclipseprojects.io/  
#client.connect("192.168.11.1",1883) -> connect tới broker của router Gl inet AR750. Router này sử dụng hệ điều hành nhúng OpenWrt trên hệ điều hành mở Linux  
Chú thích: [router Gl inet AR750 và openwrt](https://openwrt.org/toh/gl.inet/gl-ar750s), [cách cài MQTT Broker trên OpenWrt](https://www.youtube.com/watch?v=azGaeTgGddo)

# mqtt-pub1  
Mã này là một ví dụ về việc sử dụng thư viện Paho MQTT để kết nối và gửi dữ liệu tới một broker MQTT.  

 Trong đoạn mã này, chúng ta:  

 1. Import thư viện Paho MQTT và một số thư viện khác cần thiết  
 2. Thiết lập tên cho client MQTT của chúng ta (trong đoạn mã là "Temperature_Inside")  
 3. Kết nối tới broker MQTT bằng cách sử dụng địa chỉ của broker MQTT (trong đoạn mã là "mqtt.eclipseprojects.io")  
 4. Sử dụng một vòng lặp vô hạn để tạo ra một số ngẫu nhiên trong khoảng từ 20 đến 21 độ C (randNumber)  
 5. Gửi giá trị ngẫu nhiên này đến topic "TEMPERATURE" trên broker MQTT bằng cách sử dụng phương thức publish()  
 6. In ra giá trị vừa gửi và topic tương ứng  
 7. Ngủ trong 1 giây trước khi tiếp tục vòng lặp  
   
 Đoạn mã này có thể được sử dụng để gửi dữ liệu nhiệt độ từ một cảm biến nhiệt độ (hoặc bất kỳ thiết bị nào khác) tới một broker MQTT để lưu trữ hoặc xử lý dữ liệu.  
 
 # mqtt-pub2
 Tương tự như mqtt-pub1, code này dùng để gửi giá trị nguyên ngẫu nhiên từ 0-9 cho nhiệt độ ngoài trời  
   
# mqtt-sub
Mã này là một ví dụ về việc sử dụng thư viện Paho MQTT để kết nối tới một broker MQTT, đăng ký theo dõi một topic, và xử lý dữ liệu khi nhận được tin nhắn từ topic đó.  
  
Trong đoạn mã này, chúng ta:  
  
1. Định nghĩa một hàm on_message để xử lý tin nhắn khi nhận được từ broker MQTT. Trong ví dụ này, hàm sẽ chỉ in ra nội dung của tin nhắn được nhận từ topic đã đăng ký theo dõi.  
2. Thiết lập tên cho client MQTT của chúng ta (trong đoạn mã là "Smartphone")  
3. Kết nối tới broker MQTT bằng cách sử dụng địa chỉ của broker MQTT (trong đoạn mã là "mqtt.eclipseprojects.io")  
4. Bắt đầu một vòng lặp để giữ kết nối MQTT được mở (sử dụng phương thức loop_start())  
5. Đăng ký theo dõi topic "TEMPERATURE" trên broker MQTT bằng cách sử dụng phương thức subscribe()  
6. Thiết lập hàm on_message() được gọi khi nhận được tin nhắn trên topic đã đăng ký theo dõi   
7. Ngủ trong 30 giây trước khi dừng vòng lặp (sử dụng phương thức sleep())  
8. Dừng vòng lặp MQTT (sử dụng phương thức loop_stop())  
Đoạn mã này có thể được sử dụng để đăng ký theo dõi các giá trị nhiệt độ (hoặc bất kỳ dữ liệu nào khác) được gửi từ một cảm biến nhiệt độ tới một broker MQTT và xử lý các giá trị đó trên một thiết bị khác (như một smartphone).
