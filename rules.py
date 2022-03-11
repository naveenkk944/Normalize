US_STATE_NAMES = (
    'Alabama',
    'Alaska',
    'Arizona',
    'Arkansas',
    'California',
    'Colorado',
    'Connecticut',
    'Delaware',
    'Florida',
    'Georgia',
    'Hawaii',
    'Idaho',
    'Illinois',
    'Indiana',
    'Iowa',
    'Kansas',
    'Kentucky',
    'Louisiana',
    'Maine',
    'Maryland',
    'Massachusetts',
    'Michigan',
    'Minnesota',
    'Mississippi',
    'Missouri',
    'Montana',
    'Nebraska',
    'Nevada',
    'New Hampshire',
    'New Jersey',
    'New Mexico',
    'New York',
    'North Carolina',
    'North Dakota',
    'Ohio',
    'Oklahoma',
    'Oregon',
    'Pennsylvania',
    'Rhode Island',
    'South Carolina',
    'South Dakota',
    'Tennessee',
    'Texas',
    'Utah',
    'Vermont',
    'Virginia',
    'Washington',
    'West Virginia',
    'Wisconsin',
    'Wyoming'
)

ORG_NORM_PATTERN = [  
        # OPCO specific Prefix
          (r'(EBS\s*-)(.*)', r'\2')
        , (r'(HY[AT]\s*-)(.*)', r'\2')
        # Punctuations
        , (',', ' ')
        , (':', ' ')
        ,('/', ' ')
        ,('', ' ')
        , (r'\.', ' ')
        , (r'-', '')
        , (r"'", ' ')
        , (r'"', ' ')
        , (r'"', ' ')
        , (r'>+', '')
        , (r';+', '')
        , (r'\|+', '')
        
        # Stop words
        , ('the', '')
        , ('to', '')
        , ('and', '')
        , ("&"," ")
        , ('of', '')
        , ('for', '')
        # Incorporation
        ,(r'CO\.K',"")
        , (r'(incorp)\w*\b', '')
        , (r'incorp\s+incorp', '')
        , ('incor', '')
        , (r'inc\s+inc', '')
        , (r'U\.?S\.?[A]\.?\s+INC[O][R][P]O?R?A?T?E?D?', '')
        , (r'US[A]\.?\s+INC\.?', '')
        , (r'US$', '')
        ,(r'U\.S\.A\.',"")
        ,(r'USA',"")
        # Co
        , ('company', '')
        # Corp
        , ('cor', '')
        , (r'(corpor)\w*\b', '')
        , ('corporation', '')
        , (r'CO\.*,*\s+LTD\.*', '')
        , (r'CO\.*\s+OP\.*', '')
        , (r'CO', '')
        ,(r"CORP","")
        # Ltd
        , (r'limit[e][d]', '')
        # Co Ltd
        , (r'company\s+limited', '')
        , (r'co.,ltd', '')
        ,(r'ltd', '')
        ,(r'ltda', '')
        # Inc Ltd
        , (r'incorp\s+limited', '')
        # Pty Ltd
        , (r'PT[EY]\.*\s*L[I]?[M]?[I]?T[E]?[D]?\.?', '')
        # SAS
        , (r'S\s*A\s*S$', '')
        # SA
        , (r'SICAR', '')
        # SARL
        , (r'S\s*[\.]?A[\.]?\s*R[\.]?\s*L', '')
        ,(r'L\.L\.P',"LLP")
        # LP
        , (r'\bL\.?\s*P\.?\b', '')
        # SDN BHD
        , (r'SDN.?\s*BHD.?', '')  
        # International
        , (r'int[l]', 'international')
        , (r'interna\w+', 'international')
        , (r"INT'L", 'international')
        
        # National
        , (r'nat[l]', 'national')
        # ULC - UnLimited Compnay        
        , (r'ULC$', '')     
        # USA
        , (r'US[A]\.?', '')
        , (r'US$', '')
        # Remove anythin in () 
        , (r'(\w*)\(\w*\)(\w*)', r'\1 \2')
        , (r'(\w*)\(\w*\s*\)$', r'\1')
        # Extra cleaning
        , (r'NO\.', 'NO')    
        , ('INDUST', 'INDUSTRY' )        
        , ('SOUTHWEST', ' ')
        , ('TECHNOLOGIES', 'TECHNOLOGY')   
        , (r'^\s*(\d+)(.*?)(\1)+\s*$', r'\2')  
        , (r'(.*?)\s*([/]\w{0,3}\s*$)', r'\1')
        ,(r'GMBH & CO. KG',"")
        ,(r'Branch',"")
        ,(r'S\.A\.S',"")
        ,(r'SAS',"")
        ,(r'AB',"")   
        ,(r'GMBH',"")  
        ,(r'GMBH_',"")
        ,(r'AG',"")
        ,(r'OY',"")
        ,(r'BV',"")
        ,(r'INCE',"")
        ,(r'SPA',"")
        ,(r'KK',"")
        ,(r'OHG',"")
        ,(r'S\.A\.S',"")
        ,(r'SAS',"")
         ,(r'S\.P\.A',"")
        ,(r'B\.V\.',"")
        ,(r'B\.V',"")
        ,(r'INC\.',"")
        ,(r'INC',"")
        ,(r'INC_',"")
        
        ,(r'LT',"")
        ,(r'LLC',"")
        ,(r'PTY',"")
        ,(r'N\.V?\.',"")
        ,(r'KG',"")
        ,(r'e\.k?\.',"")
        , ('ENTERPRISES', 'ENTERPRISE' )  
        ,(r'SRL',"")
        ,(r'S\.R\.L',"")
        ,(r'DIVISION',"DIV")
        ,(r'SA',"")
        ,(r'S\.A\.',"")
        ,(r'S A',"")
        ,(r'LLP',"")
        ,(r'LLC',"")
        ,(r'INK',"")
        ,(r'CO\.,LT?D',"")
        ,(r'N\.V\.',"")
        ,(r'COM+$',"")
        ,(r'N\.V',"")
        ,(r'N V',"")
        ,(r'International',"")
        ,(r'SERVICES',"SERVICE")
        ,(r'SYSTEMS',"SYSTEM")
        ,(r'PRODUCTS',"PRODUCT")
        ,(r'SOLUTIONS',"SOLUTION")
        ,(r'DISTRIBUTORS',"DISTRIBUTOR")
        ,(r'STORES',"STORE")
        ,(r'SPECIALISTS',"SPECIALIST")
        ,(r'RACCORDS',"RACCORD"),(r'INDUSTRIES',"INDUSTRIE"),(r'FUELLING',"FUELING"),(r'CENTRE',"CENTER")
        ,(r'CHEMICALS',"CHEMICAL"),(r'EXPRESSAS',"EXPRESS"),(r'EXPRESSES',"EXPRESS"),(r'plastics',"plastic"),(r'TOOLS',"TOOL"),(r'METALL',"METAL"),(r'SPECIALY',"SPECIALITY"),(r'FABRICATIONS',"FABRICATION"),(r'ADHESIVES',"ADHESIVE"),(r'elettroniche',"elettronic"),(r'CASTINGS',"CASTING"),(r'holdings',"holding"),(r'equipments',"equipment"),(r'alimenticia',"alimenticias"),(r'industria',"industrias")
        ,(r'SCIENCES',"SCIENCE"),(r'ENVIRONMENTS',"ENVIRONMENT"),(r'MAINTENANCES',"MAINTENANCE"),(r'COMBUSTIVEIS',"COMBUSTIVEI"),(r'offices',"office"),(r'BANKS',"BANK"),(r'designs',"design"),(r'FINANCES',"FINANCE"),(r'LDT',""),(r'TELECOMS',"TELECOM")
        
        ,(r'advogados',"avogados"),(r'springs',"spring"),(r'WB',""),(r'poors',"poor"),(r'PROBES',"PROBE"),(r'ENVIROMENTS',"ENVIRONMENTS"),(r'PARCELS',"PARCEL"),(r'ELCTRNIC',"ELECTRONIC"),(r'BENEFITS',"BENEFIT")
        ,(r'MARKETS',"MARKET"),(r'FLAGS',"FLAG"),(r'FANS',"FAN"),(r'NC',""),(r'SLOLUTIONS',"SOLUTIONS"),(r'AUTOMOTIVAS',"AUTOMOTIVA"),(r'ME',""),(r'MT',""),(r's\.r',""),(r'IN',"")
        #,(r'',""),(r'',""),(r'',""),(r'',""),(r'',"")
        
        ,(r'PVT',"")
        ,(r'LTDD',"")
        ,(r'LLC',"")
        ,(r'UK',"")
        ,(r'U\.S\.A\.',"")
        ,(r'USA',"")
        ,(r'CO',"")

        
]

US_STATE_PARENTHESIS_RE = r' ({})$'.format(
    '|'.join('\(\s*{}\s*\)'.format(state) for state in US_STATE_NAMES)
)