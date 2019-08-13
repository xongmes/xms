
rmb_value = input('请输入人民币(CNY)金额: ')

usd2rmb = 6.77

usd_value = eval(rmb_value) / usd2rmb

print('可兑换的美元(USD)金额: ', usd_value)