# აქ ჩაწერე რამდენი ბავშვი დადის კვირში 1-ხელ 2-ჯერ 3-ჯერ და 4-ჯერ
kvirashi_1xel_raodenoba = 8
kvirashi_2jer_raodenoba = 8
kvirashi_3jer_raodenoba = 1
kvirashi_4jer_raodenoba = 0

kvirashi_1xel = kvirashi_1xel_raodenoba * 1
kvirashi_2jer = kvirashi_2jer_raodenoba * 2
kvirashi_3jer = kvirashi_3jer_raodenoba * 3
kvirashi_4jer = kvirashi_4jer_raodenoba * 4


razmelebis_raodenoba = kvirashi_1xel + kvirashi_2jer + kvirashi_3jer + kvirashi_4jer

speed_count = ((kvirashi_1xel_raodenoba) + (kvirashi_2jer_raodenoba * 2) + (kvirashi_3jer_raodenoba * 3) + (kvirashi_4jer_raodenoba * 4))


if speed_count <= 10:
    wage_per_speed = 6.75
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 15:
    wage_per_speed = 7
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 20:
    wage_per_speed = 7.25
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 25:
    wage_per_speed = 7.5
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 30:
    wage_per_speed = 7.75
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 35:
    wage_per_speed = 8
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 40:
    wage_per_speed = 8.25
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 45:
    wage_per_speed = 8.5
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
elif speed_count <= 50:
    wage_per_speed = 8.75
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))
else:
    wage_per_speed = 9
    print((kvirashi_1xel * wage_per_speed) + (kvirashi_2jer * wage_per_speed) + (kvirashi_3jer / 3 * 2.66 * wage_per_speed) +(kvirashi_4jer / 4 * 3.66 * wage_per_speed))