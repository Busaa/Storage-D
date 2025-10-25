
def read_genome_file(file_path: str) -> str:
    """
    This fucntion receves a file path as a string and reads and return the frist contig DNA sequence in the file
    read_genome_file(file_path)-> dna
    file_path: the path to the fasta or raw genome sequence file
    dna: only the DNA sequence of the organism
    """
    dna=""
    with open(file_path, "r") as file:
        header= file.readline().strip()
        
        if header.startswith(">"):
            print("Reading sequence of:", header)
        
        for line in file:
            if line.startswith(">"):
                break
            dna += line.strip()
        
        else:
            print("Reading sequence from genome input")
            dna = header
            for line in file:
                dna+= line.strip()
        
        dna = dna.replace(" ", "").replace("\n", "")
        print("Genome size:", len(dna),"bases")
        dna = dna.upper()
    return dna 

def find_seq_in_genome(genome: str, sequence: str) -> bool:
    """
    This fuction is comparing a sequence and the genome of an organism, trying to see if the sequence is a nullomer or not.
    brute_validate_nullomer(genome, sequence) -> boolean
    genome: the dna sequence of the organism storing the dna
    sequence: the sequence beaing generated and validates for storaging data
    boolean: True, is not a nullomer the sequence was fonde. False, the sequence is a nullomer
    """
    if sequence in genome:
        return True
    else:
        return False
    