sample_list = [21, 55, 18, 33, 24, 22, 68, 35, 79]
length = len(sample_list)
chunk_size = int(length / 3)

start = 0
end = chunk_size
for i in range(1,4):
    list_chunk = sample_list[start:end]
    print(f"Chunk-{i} = {list(reversed(list_chunk))}")
    start = end
    end += chunk_size