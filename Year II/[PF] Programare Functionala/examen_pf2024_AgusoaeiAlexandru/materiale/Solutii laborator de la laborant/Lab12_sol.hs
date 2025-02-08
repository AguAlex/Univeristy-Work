
--1.

data List a = Nil
            | Cons a (List a)
        deriving (Eq, Show)

instance Functor List where
    fmap _ Nil = Nil 
    fmap f (Cons a1 list) = Cons (f a1) (fmap f list)

instance Applicative List where
    pure a1 = Cons a1 Nil  
    Nil <*> listElem = Nil 
    Cons f listf <*> listElem = lappend (fmap f listElem) (listf <*> listElem)
        where 
            lappend Nil list = list 
            lappend (Cons a list1) list2 = Cons a (lappend list1 list2)

f = Cons (+1) (Cons (*2) Nil)
v = Cons 1 (Cons 2 Nil)
test1 = (f <*> v) == Cons 2 (Cons 3 (Cons 2 (Cons 4 Nil)))


--2. 

--a)
data Cow = Cow {
        name :: String
        , age :: Int
        , weight :: Int
        } deriving (Eq, Show)
        
noEmpty :: String -> Maybe String
noEmpty "" = Nothing
noEmpty str = Just str

noNegative :: Int -> Maybe Int
noNegative n 
    | n >= 0 = Just n
    | otherwise = Nothing


test21 = noEmpty "abc" == Just "abc"
test22 = noNegative (-5) == Nothing
test23 = noNegative 5 == Just 5

--b)
-- Validating to get rid of empty
-- strings, negative numbers
cowFromString :: String -> Int -> Int -> Maybe Cow
cowFromString name' age' weight' =
    case noEmpty name' of
        Nothing -> Nothing
        Just nammy -> case noNegative age' of
                        Nothing -> Nothing
                        Just agey -> case noNegative weight' of
                                        Nothing -> Nothing
                                        Just weighty -> Just (Cow nammy agey weighty)

--c)
cowFromString' :: String -> Int -> Int -> Maybe Cow
cowFromString' name' age' weight' = Cow <$> noEmpty name' <*> noNegative age' <*> noNegative weight'

cowFromString'' :: String -> Int -> Int -> Maybe Cow
cowFromString'' name' age' weight' = fmap Cow (noEmpty name') <*> noNegative age' <*> noNegative weight'


test24 = cowFromString "Milka" 5 100 == Just (Cow {name = "Milka", age = 5, weight = 100})
test25 = cowFromString' "Milka" 5 100 == Just (Cow {name = "Milka", age = 5, weight = 100})
test26 = cowFromString "Milka" (-5) 100 == Nothing
test27 = cowFromString' "" 5 (-80) == Nothing


--3.

newtype Name = Name String deriving (Eq, Show)

newtype Address = Address String deriving (Eq, Show)

data Person = Person Name Address
    deriving (Eq, Show)

--a)
validateLength :: Int -> String -> Maybe String
validateLength maxLen s = if (length s) > maxLen then Nothing else Just s

test31 = validateLength 5 "abc" == Just "abc"

--b)
mkName :: String -> Maybe Name
mkName s = case validateLength 25 s of 
           Nothing -> Nothing 
           Just s -> Just (Name s)

mkAddress :: String -> Maybe Address
mkAddress a = case validateLength 100 a of 
                Nothing -> Nothing 
                Just a -> Just (Address a)

test32 = mkName "Gigel" == Just (Name "Gigel")
test33 = mkAddress "Str Academiei" == Just (Address "Str Academiei")

--c)
mkPerson :: String -> String -> Maybe Person
mkPerson n a =
    case mkName n of
        Nothing -> Nothing
        Just n' -> case mkAddress a of
                    Nothing -> Nothing
                    Just a' -> Just $ Person n' a'

test34 = mkPerson "Gigel" "Str Academiei" == Just (Person (Name "Gigel") (Address "Str Academiei"))


--d)
mkName2 :: String -> Maybe Name
mkName2 s = fmap Name $ validateLength 25 s

mkAddress2 :: String -> Maybe Address
mkAddress2 a = fmap Address $ validateLength 100 a

mkPersonApp :: String -> String -> Maybe Person
mkPersonApp n a = Person <$> mkName2 n <*> mkAddress2 a 

