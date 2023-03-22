person = int(input('MT 인원수: '))
amount = int(input('1인당 생수 개수: '))


wtotal = person * amount
pack = wtotal // 15
bottle = wtotal % 15
total_cost = (pack * 10000) + (bottle * 900)

print('\n필요한 생수 개수 %d개' % wtotal)
print('생수 팩 구매량 %d개, %d원' % (pack, pack * 10000))
print('생수 낱개 구매량 %d개, %d원' % (bottle, bottle * 900))
print('생수 총 구매 비용 %d원' % total_cost)
