import TC.Temperatureconversion as tc

celsius = input(">请输入摄氏度数值： ")
print("%s 摄氏度 = %.3f 华氏度" %(float(celsius),tc.ctf(float(celsius))))

fahrenheit = input(">请输入华氏度数值：")
print("%s 华氏度 = %.3f 摄氏度" %(float(fahrenheit), tc.ftc(float(fahrenheit))))
