var quickSort = function(arr) {
    if(arr.length < 2) return arr;

    var pivot = arr.length/2>>2;

    for(var i = 0; i < pivot; i++){
        if(arr[i] > pivot){
            var left = arr[i];
            break;
        }
    }

    for(var i = arr.length - 1; i > pivot; i--){
        if(arr[i] < pivot){
            var right = arr[i];
            break;
        }
    }

    var temp = left;
    left = right;
    right = temp;

    var smaller = arr.slice(0, pivot);
    var larger = arr.slice(pivot, arr.length);

    return quickSort(smaller).concat(quickSort(larger));
};