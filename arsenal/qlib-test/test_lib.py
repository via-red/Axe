import qlib
# region in [REG_CN, REG_US]
from qlib.data import D
from qlib.data.filter import NameDFilter

provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
# qlib.init(provider_uri=provider_uri, region=REG_CN)
qlib.init(provider_uri='~/.qlib/qlib_data/cn_data')
# 交易日历
start_time = '2012-01-01'
end_time = '2022-12-31'
calendar = D.calendar(start_time=start_time, end_time=end_time, freq='day')
print(type(calendar))
print(calendar)

# 将给定的市场名称解析为股票池配置
print(D.instruments(market='all'))
# 获取成分股
instruments = D.instruments(market='csi300')
print(D.list_instruments(instruments=instruments, start_time=start_time, end_time=end_time, as_list=True))

# 名称过滤器从基础市场加载动态工具
nameDFilter = NameDFilter(name_rule_re='SH[0-9]{4}55')
instruments = D.instruments(market='csi300', filter_pipe=[nameDFilter])
print(D.list_instruments(instruments=instruments, start_time=start_time, end_time=end_time, as_list=True))
