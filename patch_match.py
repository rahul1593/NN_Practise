'''
	Image Zoom Finding
	
	This program finds the zoom ratio for any patch of image_near in image_far.
	It uses variable filter size whichever gives the best match for the selected patch.
'''


# 
# Fromula for calculaing distance of patch
# 
# zoom, z = b/a
# where b, a = height of object in image_near, image_far
# 
# The distance for the patch is given by..
# d = m/(1 - (1/z))
# where m is distance between the cameras (camera_d)
# 

class DepthMap:
	
	def __init__(self, image_near, image_far, filter_sizes, camera_displacement):
		self.image_near = image_near
		self.image_far = image_far
		self.filter_sizes = filter_sizes
		self.camera_displacement = camera_displacement
	
	
	'''
		Return distance in meters, for given magnification(z) and camera displacement(in meters)
	'''
	def __getDistance(self, z):
		return (self.camera_displacement / (1 - (1/z)))

	'''
		@param img_near_patch_pos: tuple containing x,y index of the patch
		Returns the magnification ratio for each patch of input image_near in given range in image_far
	'''
	def __getMagnification(self, img_near_patch_pos):
		nx, ny = tuple(img_near_patch_pos)

	'''
		Returns the depth map calculated by using image_near and image_far
	'''
	def get():
		# > read a patch of filter size from image_near
		# > Starting from the center scan the right half
		# > Starting from the center scan the left half
		# > Combine the left and right halfs
		# > return the depth map

# size of square filters to be used for matching
filter_sizes = [2, 3, 4, 5, 6, 7, 8]

# assuming image resolution to be 1280x720
image_near = cv2.imread('path/to/image_close.jpg')
image_far = cv2.imread('path/to/image_far.jpg')

# assuming cameras to be placed just in front of other and one in front to be invisible ;)
#distance between the camera_far and camera_near in meters
camera_d = 0.01
