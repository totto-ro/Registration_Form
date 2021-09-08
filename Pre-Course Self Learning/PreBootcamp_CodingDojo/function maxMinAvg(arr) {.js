function maxMinAvg(arr) {
    var arrnew = [];
    
    for(var i = 0; i < arr.length; i++)
    {
        
        var max = arr[0];
        for(var a = 0; a < arr.length; a++){
            if(max < arr[a]){
            max = arr[a];
        }
        var min = arr[0];
        for(var b = 0; b < arr.length; b++){
        if(min > arr[b]){
            min = arr [b];
        }
        var aveg = arr[0];
        var sum = 0;
        for(var c = 0; c < arr.length; c++){
            sum =  sum + arr[c];
            aveg = sum / arr.length;
        }
        }
        }
    }
    arrnew.push(max);
    arrnew.push(min);
    arrnew.push(aveg);
    return arrnew; 
}