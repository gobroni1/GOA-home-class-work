co = 0
cy = 0
cr = 0

text = "day13-🟡 | day14-🟡| day16-hw-🟠| day18-hw-🟡 | day25-cw-hw-🟠| day30-hw-🟡| day31-hw-🔴| day39-hw-🟠|day40-hw-🔴|day43-hw-🟡|day44-hw-🔴| day45-hw-🔴| day49-cw-🟠| day50-cw-🟡| day54-cw-hw-4🟠|day64-🔴|day65-hw-🟠|day66-hw-🟠|day67-hw-🟠|day68-cw-🟠|day68-hw-🟠|day69-🔴|day70-hw-🟠|day72-hw-🟠|"

for i in text:
    if i == "🟡":
        cy+= 1
    elif i == "🟠":
        co+= 1
    elif i == "🔴":
        cr+= 1
        
print(100-(co+cy+cr))