-- this function will take a number and return whether it is a square or not
isSquare :: Int -> Bool 
isSquare x = x == (floor (sqrt (fromIntegral x)))^2

-- this is the main function
final :: Int -> Int 
final x = acc 1 3 2 x 0

acc :: Int -> Int -> Int -> Int -> Int -> Int
acc startingPoint endingPoint steps upperBound accumulator
    | startingPoint == upperBound = accumulator + upperBound^2
    | otherwise = acc endingPoint (endingPoint+2) (steps + 2) upperBound (accumulator + acc' steps (fromIntegral (startingPoint^2)) (fromIntegral (endingPoint^2)))

acc' :: Int -> Int -> Int -> Int
acc' steps startingPoint endingPoint = sum [startingPoint, startingPoint + steps .. (endingPoint-1)]