   my_args = {'clip':VideoFileClip('test.mp4'), 'bottom': 10, 'right': 10, 'opacity': 10}
    myFunc = returnFunc('margin',my_args)

    # subClip1 = (subClip1\n",
    #     .fx( VideoFileClip.set_position, ("right\",\"bottom\")     )\n",
    #     .fx( VideoFileClip.set_start,   (subClip1_StartTime)    )\n",
    #     .fx( VideoFileClip.subclip,  (0, subClip1_Duration)     )\n",
    #     .fx( vfx.resize, 0.25)\n",
    #     .fx( vfx.margin, bottom=10, right=10, opacity=0))\n",
    
    
    # vfx.f
    # "#subClip2_StartTime = duration * .60\n",
    # "#subClip2_Duration = min(    (duration * .30), subClip2.duration)\n",


    # if __name__ == "__main__": 
    #     print(vfx.margin)

    #     FxObjs = vfx.margin


    inFile = "C:/Users/jason/OneDrive/Documents/repos/OriginCameras/_Input/"
    outFile = "C:/Users/jason/OneDrive/Documents/repos/OriginCameras/test.mp4"
    #allFx.margin.margin.
    clip1 = VideoFileClip(r"C:\Users\jason\OneDrive\Documents\repos\OriginCameras\_Input\SC00001\Camera001\20180525_162624.mp4")
    #newclip = (clip1.fx( vfx.margin, bottom=10, right=10, opacity=0))
    myFunc = returnFunc('margin')
    
    newclip = (clip1.fx( myFunc, my_args))

    #print(VideoFileClip.callable('margin'))
    newclip.write_videofile(outFile)

    # if hasattr(VideoFileClip, 'marsgin'): #and callable(Test.x):
    #     print ("Método 'x' existe")