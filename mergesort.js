var merge = function(left, right) {
    var merged = [];
    while(left.length && right.length){
        if(left[0] <= right[0]){
            merged.push(left.shift());
        }else{
            merged.push(right.shift());
        }   
    }
    while(left.length){
        merged.push(left.shift());
    }
    while(right.length){
        merged.push(right.shift());
    }
    return merged;
};

var mergeSort = function(arr) {

    if(arr.length < 2) return arr;

    var middle = arr.length>>1;
    var left = arr.slice(0, middle);
    var right = arr.slice(middle, arr.length);

    return merge(mergeSort(left), mergeSort(right));
};

mergeSort([99, 2, 5, 3])