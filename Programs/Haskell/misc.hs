suma :: Integer -> Integer -> Integer
suma x y = x + y

doble :: Integer -> Integer
doble x = x * 2

movHead :: [a] -> [a]
movHead  (x:xs)= xs ++ [x]

factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial(n-1)

largo :: [a] -> Integer
--largo [] = 0
--largo (x:xs) = 1 + largo xs
largo xs = foldr (\x -> (+) 1) 0 xs

media3 :: Integer -> Integer -> Integer -> Float
media3 x y z = fromIntegral (x+y+z)/3 --Puedo usar fromIntegral para convertir un Integer a Float

sumaMonedas :: Integer -> Integer -> Integer -> Integer -> Integer -> Integer
sumaMonedas a b c d e = 1*a+2*b+5*c+10*d+20*e

volumenEsfera :: Float -> Float
volumenEsfera r = ((4.0/3.0)*pi) * r

areaDeCoronaCircular :: Float -> Float -> Float
areaDeCoronaCircular r1 r2  | r1 > r2 = pi * (r1^2 - r2^2)
                            | otherwise = pi * (r2^2 - r1^2)

ultimaCifra :: Integer -> Integer
ultimaCifra x = rem x 10

maxTres :: Integer -> Integer -> Integer -> Integer
maxTres x y z = max x (max y z)

xor1 :: Bool -> Bool  -> Bool
xor1 x y | x == y = True
         | otherwise = False

-- movHeadn ::Integer -> [a] -> [a]
movHeadn n (x:xs) = drop n (x:xs) ++ take n (x:xs)



