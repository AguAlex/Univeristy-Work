data Fuel a = Fuel {getFuel :: Int -> Int -> Maybe(Int, a)}

instance Monad (Fuel a) where
    return = pure
    (Fuel r) >>= f = Fuel (\a b ->)