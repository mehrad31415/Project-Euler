
module MyHW
where


isPrime :: Int -> Bool
isPrime n = n > 1 && all (\x -> mod n x /= 0) [2..n-1]

produce :: Int -> Int -> Int -> Int
produce a b n = n^2 + a*n + b

iter :: Int -> Int -> Int -> (Int, Int, Int)
iter a b n | isPrime (produce a b n) = iter a b (n+1)
           | otherwise = (a, b, n-1)

allNum :: [(Int, Int, Int)]
allNum = [iter a b 0 | a <- [-999..999], b <- [-1000..1000]]

f = foldl (\(a1, b1, c1) (a2, b2, c2) -> if c1 > c2 then (a1, b1, c1) else (a2, b2, c2)) (0, 0, 0) allNum

final :: Int
final = (\(a, b, c) -> a*b) f

maxConsecutivePrimes :: Int 
maxConsecutivePrimes = (\(a, b, c) -> c) f