#while True: 
    #print("input.rotation(Rotation.PITCH)" + "input.rotation(Rotation.ROLL)" )
    #if input.rotation(Rotation.PITCH) <10 :
        #light.set_pixel_color(2, light.rgb(0,255,0))
    #else:
        #light.clear()
    #if input.rotation(Rotation.ROLL) <10 :
        #light.set_pixel_color(7, light.rgb(0,255,0))
while True:
    if input.acceleration(Dimension.Y) <10 :
        light.set_pixel_color(2, light.rgb(0,255,0))
    else:
        light.clear()
    if input.acceleration(Dimension.X) <10 :
        light.set_pixel_color(7, light.rgb(0,255,0))
    else:
        light.clear()
    if input.acceleration(Dimension.Z) < 10:
        light.set_pixel_color(4, light.rgb(0,255,0))
        light.set_pixel_color(5, light.rgb(0,255,0))
    else:
        light.clear()