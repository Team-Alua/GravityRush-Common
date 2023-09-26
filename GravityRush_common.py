from inc_noesis import *
import noesis
import rapi
import os


def registerNoesisTypes():
    loadNameHashDict()
    return 1

FNV1A_32_OFFSET = 0x811c9dc5
FNV1A_32_PRIME = 0x01000193

HASHMAPS = [r"C:\Users\caine\Documents\GitHub\Gravity\Development\Noesis\GR_Hash_Dict\GR2_String_Hashmap.txt"]

    
def fnv1a_32_str(string):
    # Set the offset basis
    hash = FNV1A_32_OFFSET

    # For each character
    for character in string:
        # Xor with the current character
        hash ^= ord(character)

        # Multiply by prime
        hash *= FNV1A_32_PRIME

        # Clamp
        hash &= 0xffffffff

    # Return the final hash as a number
    hash = hex(hash)[2:]
    if len(hash) == 7:
        hash = '0' + hash
    hash = hash[6:8]+hash[4:6]+hash[2:4]+hash[0:2]
    return hash

    
def loadNameHashDict():
    if len(gr_namehash) == 0:
        count = 0
        for HASHMAP_PATH in HASHMAPS:
            if not os.path.exists(HASHMAP_PATH):
                print("Can't find dictionary file %s" % HASHMAP_PATH)
                continue
            txt = open(HASHMAP_PATH, mode='r', encoding="utf-8")
            for line in txt:
                # print(line)
                line = line.split('\n')[0]
                try:
                    gr_namehash[line.split('\t')[1]] = line.split('\t')[
                        0]
                    #print("Dictionary loaded: %s with name %s" % (line.split('\t')[1], line.split('\t')[0]))
                except:
                    gr_namehash[line.split('\t')[0]] = fnv1a_32_str(
                        line.split('\t')[0])
                    print("Dictionary calculated: %s %s" % (
                        line.split('\t')[0], gr_namehash[line.split('\t')[0]]))
                count += 1
            txt.close()
        print("Dictionary loaded with %i strings" % count)
    else:
        print("Dictionary alread loaded")

def getNameFromHash(nameHash):
    nameHash = hex(nameHash)[2:]
    if len(nameHash) == 7:
        nameHash = '0' + nameHash
    nameHash = nameHash[6:8]+nameHash[4:6]+nameHash[2:4]+nameHash[0:2]
    try:
        return gr_namehash[nameHash]
    except:
        # print("Can't find string of hash %s" % nameHash)
        return nameHash
    
gr_namehash = {}