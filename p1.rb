def digital_root(num) 
    return num if num < 10
    digital_root((num % 10) + (num / 10))
end

