from fpdf import FPDF

def nextPermutation(nums):
	"""
	:type nums: List[int]
	:rtype: None Do not return anything, modify nums in-place instead.
	"""
	pivotFirst=-1
	i=len(nums)-1
	tmp=nums[-1]
	while i>=0:
		if nums[i]>=tmp:
			tmp=nums[i]
			i-=1
		else:
			pivotFirst=i
			break
	print(pivotFirst)
	if pivotFirst==-1:
		nums.reverse()
		return
	pivotFirst=i
	pivotSecond=-1
	j=len(nums)-1
	while(j>pivotFirst):
		if nums[j]>nums[pivotFirst]:
			pivotSecond=j
			break
		j-=1

	print(pivotFirst,pivotSecond)

	nums[pivotSecond],nums[pivotFirst]=nums[pivotFirst],nums[pivotSecond]
	l,r = pivotFirst+1, len(nums)-1
	while l < r:
		nums[l], nums[r] = nums[r], nums[l]
		l += 1
		r -= 1

nums = [5,1,1]
print(nextPermutation(nums))
print(nums)

pdf = FPDF() # create pdf
pdf.add_page() #add page!
pdf.set_font("Arial", size=12) # font
pdf.cell(200, 10, txt=str(gotmode), ln=1, align="C") #write to pdf, They need to be strings
pdf.cell(200, 10, txt=str(gotmean), ln=1, align="C")
pdf.cell(200, 10, txt=helloworld, ln=1, align="C")

pdf.output("simple_demo.pdf") # output file