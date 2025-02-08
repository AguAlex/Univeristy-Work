int Rootkit::calcul_rating(){
    for(auto st : stringuri_semnificative){
        if(st == "Systeam Service Descriptor Table" ||
           st == "SSDT" || st == "NtCreateFile"){
            rating_impact += 100;
            break;
           }
    }
    
    for(auto imp : importuri){
        if(imp == "ntoskrnl.exe"){
            rating_impact *= 2;
            break;
        }
    }
    return rating_impact;
}