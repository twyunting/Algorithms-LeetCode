func isMajorityElement(_ nums: [Int], _ target: Int) -> Bool {    
    var middle = nums.count-1
	return nums[middle/2] == target     
}
