# import the Python Image  
# processing Library 
from PIL import Image 
import os, sys

path = "./trainA/"
dirs = os.listdir( path )
  
# Giving The Original image Directory  
# Specified 

i = 0

for item in dirs:
        if os.path.isfile(path+item):

            print(path+item)
            Original_Image = Image.open(path+item)


            
            

            ############### Image 1###########################
            # Rotate Image By 180 Degree 
            rotated_image1 = Original_Image.rotate(180) 

            rotated_image1.save('./trainA/new/100' + str(i) + '.png', 'PNG')

            i += 1

            ###################shearing#####################

            # # he matrix is represented as a tuple (a, b, c, d, e, f). For horizontal shearing, set b and e to the shear factor:
            # sheared_image1801 = Original_Image.transform((Original_Image.width + 100, Original_Image.height), Image.AFFINE, (1, 0.2, -100, 0, 1, 0))
            # # Apply horizontal shearing with a shear factor of 0.2
            # sheared_image1801.save('./img1/she1801' + '.png', 'PNG')

            # # he matrix is represented as a tuple (a, b, c, d, e, f). For horizontal shearing, set b and e to the shear factor:
            # sheared_image1802 = Original_Image.transform((Original_Image.width + 100, Original_Image.height), Image.AFFINE, (1, -0.2, -100, 0, 1, 0))
            # # Apply horizontal shearing with a shear factor of 0.2
            # sheared_image1802.save('./img1/she1802' + '.png', 'PNG')


            ###############fliping#######################

            flipped_image1801 = Original_Image.transpose(Image.FLIP_LEFT_RIGHT)  # Flip the image horizontally

            flipped_image1801.save('./trainA/new/200' + str(i) + '.png', 'PNG')

            i += 1

            ##
            flipped_image1802 = Original_Image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image horizontally

            flipped_image1802.save('./trainA/new/300' + str(i)+ '.png', 'PNG')

            i += 1


            ############################Image 2###############################
            # This Will Rotate Image By 90 Degree 
            rotated_image2 = Original_Image.rotate(90) 

            rotated_image2.save('./trainA/new/400' + str(i) + '.png', 'PNG')

            i += 1

            ###################shearing#####################

            # # he matrix is represented as a tuple (a, b, c, d, e, f). For horizontal shearing, set b and e to the shear factor:
            # sheared_image901 = Original_Image.transform((Original_Image.width + 100, Original_Image.height), Image.AFFINE, (1, 0.2, -100, 0, 1, 0))
            # # Apply horizontal shearing with a shear factor of 0.2
            # sheared_image901.save('./img1/she901' + '.png', 'PNG')

            # # he matrix is represented as a tuple (a, b, c, d, e, f). For horizontal shearing, set b and e to the shear factor:
            # sheared_image902 = Original_Image.transform((Original_Image.width + 100, Original_Image.height), Image.AFFINE, (1, -0.2, -100, 0, 1, 0))
            # # Apply horizontal shearing with a shear factor of 0.2
            # sheared_image902.save('./img1/she902' + '.png', 'PNG')


            ##############fliping#######################

            flipped_image901 = Original_Image.transpose(Image.FLIP_LEFT_RIGHT)  # Flip the image horizontally

            flipped_image901.save('./trainA/new/500' + str(i) + '.png', 'PNG')

            i += 1

            ###
            flipped_image902 = Original_Image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image horizontally

            flipped_image902.save('./trainA/new/600' + str(i) + '.png', 'PNG')

            i += 1

            ###############################Image 3############################

            # This Will Rotate Image By 270 Degree 
            rotated_image3 = Original_Image.rotate(270) 

            rotated_image3.save('./trainA/new/700' + str(i) + '.png', 'PNG')

            i += 1

            ###################shearing#####################

            # # he matrix is represented as a tuple (a, b, c, d, e, f). For horizontal shearing, set b and e to the shear factor:
            # sheared_image2701 = Original_Image.transform((Original_Image.width + 100, Original_Image.height), Image.AFFINE, (1, 0.2, -100, 0, 1, 0))
            # # Apply horizontal shearing with a shear factor of 0.2
            # sheared_image2701.save('./img1/she2701' + '.png', 'PNG')

            # # he matrix is represented as a tuple (a, b, c, d, e, f). For horizontal shearing, set b and e to the shear factor:
            # sheared_image2702 = Original_Image.transform((Original_Image.width + 100, Original_Image.height), Image.AFFINE, (1, -0.2, -100, 0, 1, 0))
            # # Apply horizontal shearing with a shear factor of 0.2
            # sheared_image2702.save('./img1/she2702' + '.png', 'PNG')


            ###############fliping#######################

            flipped_image2701 = Original_Image.transpose(Image.FLIP_LEFT_RIGHT)  # Flip the image horizontally

            flipped_image2701.save('./trainA/new/800' + str(i) + '.png', 'PNG')

            i += 1

            ##
            flipped_image2702 = Original_Image.transpose(Image.FLIP_TOP_BOTTOM)  # Flip the image horizontally

            flipped_image2702.save('./trainA/new/900' + str(i) + '.png', 'PNG')

            i += 1








