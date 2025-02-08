import Distribution.Simple.Setup (programDbPaths')

{- Monada Maybe este definita in GHC.Base 

instance Monad Maybe where
  return = Just
  Just va  >>= k   = k va
  Nothing >>= _   = Nothing


instance Applicative Maybe where
  pure = return
  mf <*> ma = do
    f <- mf
    va <- ma
    return (f va)       

instance Functor Maybe where              
  fmap f ma = pure f <*> ma   
-}


--1.
pos :: Int -> Bool
pos  x = if (x>=0) then True else False

fct :: Maybe Int ->  Maybe Bool
fct  mx =  mx  >>= (\x -> Just (pos x))

--definitie folosind notatia do:
fct' :: Maybe Int ->  Maybe Bool
fct' mx = do
  x <- mx
  Just (pos x)


--2.
--a)
--definitie folosind sabloane:
addM :: Maybe Int -> Maybe Int -> Maybe Int
addM (Just x) (Just y) = Just (x+y)
addM _ _ = Nothing

--b)
--definitie folosind operatii monadice:
addM' :: Maybe Int -> Maybe Int -> Maybe Int
addM' mx my = 
  mx >>= (\x -> my >>= (\y-> return (x+y)))

--definitie folosind notatia do:
addM'' :: Maybe Int -> Maybe Int -> Maybe Int
addM'' mx my = do
  x <- mx
  y <- my
  return (x+y)

--teste:
{-
addM (Just 4) (Just 3) 
Just 7

addM (Just 4) Nothing
Nothing

addM Nothing Nothing
Nothing
-}


--3.
cartesian_product xs ys = xs >>= ( \x -> (ys >>= \y-> return (x,y)))

--rescriere folosind notatia do:
cartesian_product' xs ys = do
  x <- xs
  y <- ys
  return (x,y)

--teste: 
--cartesian_product [1,3] [2,4]
--cartesian_product' [1,3] [2,4]
--rezultat: [(1,2),(1,4),(3,2),(3,4)]

prod f xs ys = [f x y | x <- xs, y<-ys]

--rescriere folosind notatia do:
prod' f xs ys = do
  x <- xs
  y <- ys
  return (f x y)

--teste:
--prod (*) [1,2] [3,4]
--prod' (*) [1,2] [3,4]
--rezultat: [3,4,6,8]

myGetLine :: IO String
myGetLine = getChar >>= \x ->
      if x == '\n' then
          return []
      else
          myGetLine >>= \xs -> return (x:xs)

--rescriere folosind notatia do:
myGetLine'= do
  x<-getChar
  if x == '\n' then
    return []
  else 
    do
      xs<-myGetLine'
      return (x : xs)


--4.
prelNo noin =  sqrt noin

ioNumber = do
     noin  <- readLn :: IO Float
     putStrLn $ "Intrare\n" ++ (show noin)
     let  noout = prelNo noin
     putStrLn $ "Iesire"
     print noout

--rescriere folosind notatia cu secventiere:
ioNumber' = (readLn :: IO Float) >>= \noin -> 
            putStrLn ("Intrare\n" ++ show noin) >>
            let noout = prelNo noin in
              putStrLn "Iesire" >>
              print noout


--5.
--rezolvare in fisierul mWriter_sol.hs


--6.
data Person = Person { name :: String, age :: Int }

--a)
showPersonN :: Person -> String
showPersonN p = let x =  name p in ("NAME: "++ x)

showPersonA :: Person -> String
showPersonA p = let y =  age p in ("AGE: "++ (show y))

showPerson :: Person -> String
showPerson p = let 
                 x = showPersonN p
                 y = showPersonA p                  
               in ("("++ x ++", "++y++")") 
  
--teste:
{-
showPersonN $ Person "ada" 20
"NAME: ada"

showPersonA $ Person "ada" 20
"AGE: 20"

showPerson $ Person "ada" 20
"(NAME: ada, AGE: 20)"
-}


--b)
--rezolvare in fisierul mWriter_sol.hs


--c)
newtype Reader env a = Reader { runReader :: env -> a }


instance Monad (Reader env) where
  return x = Reader (\_ -> x)
  ma >>= k = Reader f
    where f env = let a = runReader ma env
                  in  runReader (k a) env


instance Applicative (Reader env) where
  pure = return
  mf <*> ma = do
    f <- mf
    a <- ma
    return (f a)       


instance Functor (Reader env) where              
  fmap f ma = pure f <*> ma    



mshowPersonN ::  Reader Person String 
mshowPersonN  =  Reader (\person -> "NAME: " ++ name person)    

mshowPersonA ::  Reader Person String
mshowPersonA  =  Reader (\person -> "AGE: " ++ show (age person))   

--sau cu do notation:
{-
mshowPersonN ::  Reader Person String 
mshowPersonN  =  do
  person <- Reader (\env -> env) -- Preluăm mediul (Person) folosind monada Reader
  return $ "NAME: " ++ name person    

mshowPersonA ::  Reader Person String
mshowPersonA  =  do
  person <- Reader (\env -> env) -- Preluăm mediul (Person) folosind monada Reader
  return $ "AGE: " ++ show (age person)   
-}

mshowPerson :: Reader Person String
mshowPerson = do 
                personName <- mshowPersonN
                personAge <- mshowPersonA
                return ("(" ++ personName ++ ", " ++ personAge ++ ")")

--teste:
{-
runReader mshowPersonN  $ Person "ada" 20
"NAME: ada"

runReader mshowPersonA  $ Person "ada" 20
"AGE: 20"

runReader mshowPerson  $ Person "ada" 20
"(NAME: ada, AGE: 20)"
-}