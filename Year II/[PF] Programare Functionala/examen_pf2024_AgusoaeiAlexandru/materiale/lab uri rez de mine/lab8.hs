class Collection c where
    empty :: c key value
    singleton :: key -> value -> c key value
    insert :: Ord key => key -> value -> c key value -> c key value
    lookup :: Ord key => key -> c key value -> Maybe value
    delete :: Ord key => key -> c key value -> c key value
    keys :: c key value -> [key]
    values :: c key value -> [value]
    toList :: c key value -> [(key, value)]
    fromList :: Ord key => [(key,value)] -> c key value

    -- 1
    keys = map fst . toList
    values = map snd . toList
    fromList = foldr (\(k, v) acc -> insert k v acc) empty


-- 2
newtype PairList k v = PairList { getPairList :: [(k, v)] } deriving (Show)

instance Collection PairList where
    empty = PairList []
    singleton k v = PairList [(k, v)]
    insert k v (PairList pairs) = PairList $ (k, v) : filter (\(key, _) -> key /= k) pairs
    lookup k (PairList pairs) = lookupKey k pairs where 
                                lookupKey _ [] = Nothing
                                lookupKey key ((k',v):xs)
                                    | key == k' = Just v
                                    | otherwise = lookupKey key xs
    delete k (PairList pairs) = PairList $ filter (\(key, _) -> key /= k) pairs
    toList = getPairList

myPairList :: PairList String Int
myPairList = PairList [("a", 1), ("b", 2), ("c", 3)]