num = int(input("ตัวเลขที่ 1:"))
num = int(input("ตัวเลขที่ 2:"))
op = int(input("เครื่องหมาย(+,-,*,/):"))

result = 0
if op == "+":
    result == num1 + num2
elif op == "-":
    result == num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    result = num1 / num2
else:
    raise ValueError("เครื่องหมาย + - * / เท่านั้น")

print(f"{num} {oprator} {num2} = {result}")

except ValueError: #กรณีผู้ใช้ไม่พิมพ์ตัวเลข
    print("กรุณากรอกข้อมูลที่เป็นตัวเลขเท่านั้น")

except ZeroDivisionError: #กรณีผู้ใช้ใส่ตัวหารเป็น 0
    print("ไม่สามารถหารด้วยศูนย์ได้")

except Exception: #กรณีอื่นๆ
    print("ทำอะไรไม่ได้บางอย่างแต่ไม่เเน่ใจว่าคืออะไร")

else: #จะทำที่นี่ก็ต่อเมื่อไม่มี exception
    print("คำนวณข้อมูลเรียบร้อยเเล้ว")    

finally: 
    print("จบการทำงาน")