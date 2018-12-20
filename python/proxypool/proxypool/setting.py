# redis数据库地址
REDIS_HOST = '127.0.0.1'

# redis端口
REDIS_PORT = 6379

# redis密码
REDIS_PASSWORD = None

# redis orted set key
REDIS_KEY = 'proxies'

# 代理分数
# 最大
MAX_SCORE = 100
# 最小
MIN_SCORE = 0
# 新代理初始分数
INITIAL_SCORE = 10

VALID_STATUS_CODES = [200, 302]

# 代理池数量界限
POOL_UPPER_THRESHOLD = 10000

# 检查周期
TESTER_CYCLE = 20

# 获取周期
GETTER_CYCLE = 300

# 测试API

TEST_URL = 'http://httpbin.org/get'

# API配置
API_HOST = '0.0.0.0'
API_PORT = 5555

# 开关
TESTER_ENABLED = True
GETTER_ENABLED = True
API_ENABLED = True

# 最大批测试量
BATCH_TEST_SIEZ = 10