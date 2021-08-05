from django.db import migrations

IMPACTS = [
    {
        "value": "Allow people to explore their values, meanings and dreams",
        "lemma": "allow people explore value meaning dream",
        "column": 0
    },
    {
        "value": "More appropriate sexual behavior",
        "lemma": "appropriate sexual behavior",
        "column": 0
    },
    {
        "value": "More attachment to the place",
        "lemma": "attachment place",
        "column": 2
    },
    {
        "value": "Attraction of inward investments",
        "lemma": "attraction inward investment",
        "column": 1
    },
    {
        "value": "Attraction of tourism inflows",
        "lemma": "attraction tourism inflow",
        "column": 1
    },
    {
        "value": "More availability to engage in health education",
        "lemma": "availability engage health education",
        "column": 0
    },
    {
        "value": "Better awareness of community identity",
        "lemma": "better awareness community identity",
        "column": 2
    },
    {
        "value": "Better capacity to socialize",
        "lemma": "better capacity socialize",
        "column": 0
    },
    {
        "value": "Better understanding of communal meaning",
        "lemma": "better understanding communal meaning",
        "column": 2
    },
    {
        "value": "Better understanding of diversity",
        "lemma": "better understanding diversity",
        "column": 2
    },
    {
        "value": "Build community organisational capacity",
        "lemma": "build community organizational capacity",
        "column": 1
    },
    {
        "value": "Challenge conventional service delivery",
        "lemma": "challenge conventional service delivery",
        "column": 0
    },
    {
        "value": "Contribute to people\u2019s employability",
        "lemma": "contribute people employability",
        "column": 2
    },
    {
        "value": "Creation of community traditions in new towns or neighbourhoods",
        "lemma": "creation community tradition new town neighborhood",
        "column": 1
    },
    {
        "value": "Creation of jobs",
        "lemma": "creation job",
        "column": 1
    },
    {
        "value": "Develop community networks and sociability",
        "lemma": "develop community network sociability",
        "column": 0
    },
    {
        "value": "Developed contact between generations",
        "lemma": "developed contact generation",
        "column": 2
    },
    {
        "value": "Development of pride in local traditions and cultures",
        "lemma": "development pride local tradition culture",
        "column": 1
    },
    {
        "value": "Ecological sustainability",
        "lemma": "ecological sustainability",
        "column": 1
    },
    {
        "value": "Economic sustainability",
        "lemma": "economic sustainability",
        "column": 1
    },
    {
        "value": "Educational development of children",
        "lemma": "educational development child",
        "column": 2
    },
    {
        "value": "Encourage local self-reliance and project management",
        "lemma": "encourage local self reliance project management",
        "column": 1
    },
    {
        "value": "Encourage people to accept risk positively",
        "lemma": "encourage people accept risk positively",
        "column": 0
    },
    {
        "value": "Encouragement to take up education and training opportunities",
        "lemma": "encouragement take education training opportunity",
        "column": 2
    },
    {
        "value": "An enduring sentiment of joy and happiness",
        "lemma": "enduring sentiment joy happiness",
        "column": 0
    },
    {
        "value": "Enhanced intercultural contact and cooperation",
        "lemma": "enhanced intercultural contact cooperation",
        "column": 2
    },
    {
        "value": "Enhanced local identity",
        "lemma": "enhanced local identity",
        "column": 1
    },
    {
        "value": "Enhanced social cohesion",
        "lemma": "enhanced social cohesion",
        "column": 1
    },
    {
        "value": "Enrich the practice of professionals in the public and voluntary sectors",
        "lemma": "enrich practice professional public voluntary sector",
        "column": 0
    },
    {
        "value": "Erode the distinction between consumer and creator",
        "lemma": "erode distinction consumer creator",
        "column": 1
    },
    {
        "value": "Extended involvement in social activities",
        "lemma": "extended involvement social activity",
        "column": 0
    },
    {
        "value": "Facilitate the development of partnerships",
        "lemma": "facilitate development partnership",
        "column": 1
    },
    {
        "value": "Facilitate effective public consultation and participation",
        "lemma": "facilitate effective public consultation participation",
        "column": 2
    },
    {
        "value": "A forum to explore personal rights and responsibilities",
        "lemma": "forum explore personal right responsibility",
        "column": 2
    },
    {
        "value": "A forum for intercultural understanding and friendship",
        "lemma": "forum intercultural understanding friendship",
        "column": 1
    },
    {
        "value": "Greater stewardship of place",
        "lemma": "greater stewardship place",
        "column": 2
    },
    {
        "value": "Help build new skills and work experience",
        "lemma": "help build new skill work experience",
        "column": 2
    },
    {
        "value": "Help community groups raise their vision beyond the immediate",
        "lemma": "help community group raise vision beyond immediate",
        "column": 1
    },
    {
        "value": "Help involve local people in the regeneration process",
        "lemma": "help involve local people regeneration process",
        "column": 1
    },
    {
        "value": "Help offenders and victims address issues of crime",
        "lemma": "help offender victim address issue crime",
        "column": 0
    },
    {
        "value": "Help people develop their creativity",
        "lemma": "help people develop creativity",
        "column": 2
    },
    {
        "value": "Help people extend control over their own lives",
        "lemma": "help people extend control life",
        "column": 0
    },
    {
        "value": "Help people feel a sense of belonging and involvement",
        "lemma": "help people feel sense belonging involvement",
        "column": 1
    },
    {
        "value": "Help people take up or develop careers in the arts",
        "lemma": "help people take develop career art",
        "column": 2
    },
    {
        "value": "Help transform the image of public bodies",
        "lemma": "help transform image public body",
        "column": 1
    },
    {
        "value": "Help validate the contribution of a whole community",
        "lemma": "help validate contribution whole community",
        "column": 1
    },
    {
        "value": "Higher neighbourhood pride",
        "lemma": "higher neighborhood pride",
        "column": 2
    },
    {
        "value": "Higher self esteem",
        "lemma": "higher self esteem",
        "column": 0
    },
    {
        "value": "Higher social capital",
        "lemma": "higher social capital",
        "column": 2
    },
    {
        "value": "Improved ability to communicate",
        "lemma": "improved ability communicate",
        "column": 0
    },
    {
        "value": "Improved competitiveness",
        "lemma": "improved competitiveness",
        "column": 1
    },
    {
        "value": "Improved perceptions of marginalised groups",
        "lemma": "improved perception marginalized group",
        "column": 2
    },
    {
        "value": "Improved quality of life of local people",
        "lemma": "improved quality life local people",
        "column": 1
    },
    {
        "value": "Improved quality of life of people with poor health",
        "lemma": "improved quality life people poor health",
        "column": 0
    },
    {
        "value": "Improved quality of urban planning and design",
        "lemma": "improved quality urban planning design",
        "column": 1
    },
    {
        "value": "Improved sense of place",
        "lemma": "improved sense place",
        "column": 2
    },
    {
        "value": "Improved sense of well being",
        "lemma": "improved sense wellbeing",
        "column": 0
    },
    {
        "value": "Improved urban marketing",
        "lemma": "improved urban marketing",
        "column": 1
    },
    {
        "value": "Increased civic sense",
        "lemma": "increased civic sense",
        "column": 2
    },
    {
        "value": "Increased community attachment",
        "lemma": "increased community attachment",
        "column": 2
    },
    {
        "value": "Increased feeling of personal confidence",
        "lemma": "increased feeling personal confidence",
        "column": 0
    },
    {
        "value": "Increased participation in political activities",
        "lemma": "increased participation political activity",
        "column": 2
    },
    {
        "value": "Increased participation in social activities",
        "lemma": "increased participation social activity",
        "column": 2
    },
    {
        "value": "Increased participation in urban life",
        "lemma": "increased participation urban life",
        "column": 1
    },
    {
        "value": "Increased sense of belonging to the community",
        "lemma": "increased sense belonging community",
        "column": 2
    },
    {
        "value": "Increased sharing and collaborative attitude",
        "lemma": "increased sharing collaborative attitude",
        "column": 2
    },
    {
        "value": "Increased social ethic",
        "lemma": "increased social ethic",
        "column": 2
    },
    {
        "value": "More influence over how people are seen by others",
        "lemma": "influence people seen others",
        "column": 0
    },
    {
        "value": "More intense feelings of solidarity",
        "lemma": "intense feeling solidarity",
        "column": 2
    },
    {
        "value": "Involvement of residents in environmental improvements",
        "lemma": "involvement resident environmental improvement",
        "column": 1
    },
    {
        "value": "Make people feel better about where they live",
        "lemma": "make people feel better live",
        "column": 1
    },
    {
        "value": "A means of gaining insight into political and social ideas",
        "lemma": "mean gaining insight political social idea",
        "column": 2
    },
    {
        "value": "New balance between centre and periphery",
        "lemma": "new balance center periphery",
        "column": 1
    },
    {
        "value": "New cultural amenities",
        "lemma": "new cultural amenity",
        "column": 1
    },
    {
        "value": "New industry development",
        "lemma": "new industry development",
        "column": 1
    },
    {
        "value": "New leisure facilities",
        "lemma": "new leisure facility",
        "column": 1
    },
    {
        "value": "Preservation of historical heritage",
        "lemma": "preservation historical heritage",
        "column": 1
    },
    {
        "value": "Promote tolerance and contribute to conflict resolution",
        "lemma": "promote tolerance contribute conflict resolution",
        "column": 2
    },
    {
        "value": "More propensity to adopt a healthier lifestyle",
        "lemma": "propensity adopt healthier lifestyle",
        "column": 0
    },
    {
        "value": "Provide reasons for people to develop community activities",
        "lemma": "provide reason people develop community activity",
        "column": 1
    },
    {
        "value": "Provide a route to rehabilitation and integration for offenders",
        "lemma": "provide route rehabilitation integration offender",
        "column": 0
    },
    {
        "value": "Raise expectations about what is possible and desirable",
        "lemma": "raise expectation possible desirable",
        "column": 0
    },
    {
        "value": "Reduced alcohol intake",
        "lemma": "reduced alcohol intake",
        "column": 0
    },
    {
        "value": "Reduced drug addition",
        "lemma": "reduced drug addiction",
        "column": 0
    },
    {
        "value": "Reduced feeling of anxiety",
        "lemma": "reduced feeling anxiety",
        "column": 0
    },
    {
        "value": "Reduced feeling of depression",
        "lemma": "reduced feeling depression",
        "column": 0
    },
    {
        "value": "Reduced isolation by helping people to make friends",
        "lemma": "reduced isolation helping people make friend",
        "column": 0
    },
    {
        "value": "A more relaxed atmosphere in health centres",
        "lemma": "relaxed atmosphere health center",
        "column": 0
    },
    {
        "value": "Repositioning of the city image",
        "lemma": "repositioning city image",
        "column": 1
    },
    {
        "value": "Repudiation of any sort of discrimination",
        "lemma": "repudiation sort discrimination",
        "column": 2
    },
    {
        "value": "Respect for other\u2019s opinions",
        "lemma": "respect opinion",
        "column": 2
    },
    {
        "value": "Risk of gentrification",
        "lemma": "risk gentrification",
        "column": 1
    },
    {
        "value": "Social sustainability",
        "lemma": "social sustainability",
        "column": 1
    },
    {
        "value": "Stimulated interest and confidence in culture",
        "lemma": "stimulated interest confidence culture",
        "column": 2
    },
    {
        "value": "Strengthened community cooperation and networking",
        "lemma": "strengthened community cooperation networking",
        "column": 2
    },
    {
        "value": "Support to community projects",
        "lemma": "support community project",
        "column": 1
    },
    {
        "value": "Support to creative industries and clusters",
        "lemma": "support creative industry cluster",
        "column": 1
    },
    {
        "value": "Tighter social bonds in the community",
        "lemma": "tighter social bond community",
        "column": 2
    },
    {
        "value": "Transform the responsiveness of public service organisations",
        "lemma": "transform responsiveness public service organization",
        "column": 0
    },
    {
        "value": "Valorisation of local talents",
        "lemma": "valorisation local talent",
        "column": 1
    }
]

IMPACT_KEYWORDS = [
    {
        "value": "community identity enhanced"
    },
    {
        "value": "skill knowledge build"
    },
    {
        "value": "heritage heritage conservation"
    },
    {
        "value": "social bond time"
    },
    {
        "value": "greater confidence personal"
    },
    {
        "value": "develop people"
    },
    {
        "value": "economic sustainability growing"
    },
    {
        "value": "feeling solidarity isolation"
    },
    {
        "value": "aggravate feeling depression"
    },
    {
        "value": "overall sense wellbeing"
    },
    {
        "value": "quality life local"
    },
    {
        "value": "place attachment political"
    },
    {
        "value": "ability communicate thought"
    },
    {
        "value": "people employability"
    },
    {
        "value": "increased social participation"
    },
    {
        "value": "quality life increased"
    },
    {
        "value": "sense place increased"
    },
    {
        "value": "community participation support"
    },
    {
        "value": "social sustainability culture"
    },
    {
        "value": "development cultural amenity"
    },
    {
        "value": "reduced anxiety fun"
    },
    {
        "value": "recognition discrimination"
    },
    {
        "value": "organization build capacity"
    },
    {
        "value": "heritage expression historical"
    },
    {
        "value": "anxiety improve wellbeing"
    },
    {
        "value": "factor improving competitiveness"
    },
    {
        "value": "strong social bond"
    },
    {
        "value": "environment economic sustainability"
    },
    {
        "value": "project library community"
    },
    {
        "value": "study cultural amenity"
    },
    {
        "value": "part project community"
    },
    {
        "value": "danger partly gentrification"
    },
    {
        "value": "experience help create"
    },
    {
        "value": "sustainability ecological"
    },
    {
        "value": "gentrification problem"
    },
    {
        "value": "child development adolescent"
    },
    {
        "value": "gentrification exposure"
    },
    {
        "value": "cultural amenity cutting"
    },
    {
        "value": "community support local"
    },
    {
        "value": "discrimination oppression"
    },
    {
        "value": "community member project"
    },
    {
        "value": "community project instance"
    },
    {
        "value": "feel sense belonging"
    },
    {
        "value": "improvement urban design"
    },
    {
        "value": "leisure facility residence"
    },
    {
        "value": "participation preservation heritage"
    },
    {
        "value": "social capital people"
    },
    {
        "value": "sustainability ecology"
    },
    {
        "value": "reduced depression"
    },
    {
        "value": "involved regeneration process"
    },
    {
        "value": "project community organizing"
    },
    {
        "value": "competitiveness boosting"
    },
    {
        "value": "influence people perception"
    },
    {
        "value": "people feel best"
    },
    {
        "value": "job creation namely"
    },
    {
        "value": "year social activity"
    },
    {
        "value": "form discrimination"
    },
    {
        "value": "increased economic activity"
    },
    {
        "value": "professional public sector"
    },
    {
        "value": "result discrimination"
    },
    {
        "value": "enhance creativity people"
    },
    {
        "value": "life people poor"
    },
    {
        "value": "institutional discrimination"
    },
    {
        "value": "job creation employment"
    },
    {
        "value": "drug addiction irrevocably"
    },
    {
        "value": "self reliance develop"
    },
    {
        "value": "support community local"
    },
    {
        "value": "contribution whole community"
    },
    {
        "value": "community project increase"
    },
    {
        "value": "involvement community project"
    },
    {
        "value": "community project social"
    },
    {
        "value": "develop community network"
    },
    {
        "value": "promotion inward investment"
    },
    {
        "value": "new industry local"
    },
    {
        "value": "life wellbeing improved"
    },
    {
        "value": "level participation activity"
    },
    {
        "value": "preservation historical"
    },
    {
        "value": "community support arden"
    },
    {
        "value": "improving quality urban"
    },
    {
        "value": "preservation national heritage"
    },
    {
        "value": "new industry"
    },
    {
        "value": "development creative industry"
    },
    {
        "value": "community awareness"
    },
    {
        "value": "building capacity community"
    },
    {
        "value": "inward investment public"
    },
    {
        "value": "cultural amenity draw"
    },
    {
        "value": "new development market"
    },
    {
        "value": "increasing involvement activity"
    },
    {
        "value": "pride higher"
    },
    {
        "value": "community development project"
    },
    {
        "value": "people educational development"
    },
    {
        "value": "intercultural understanding city"
    },
    {
        "value": "improves sense wellbeing"
    },
    {
        "value": "project coming community"
    },
    {
        "value": "exclusion discrimination"
    },
    {
        "value": "involved sexual behavior"
    },
    {
        "value": "tradition culture also"
    },
    {
        "value": "people creativity"
    },
    {
        "value": "also creation job"
    },
    {
        "value": "increased confidence"
    },
    {
        "value": "community building capacity"
    },
    {
        "value": "training job creation"
    },
    {
        "value": "communal meaning"
    },
    {
        "value": "increasing civic"
    },
    {
        "value": "network bond social"
    },
    {
        "value": "inward investment introduction"
    },
    {
        "value": "support social activity"
    },
    {
        "value": "identity awareness"
    },
    {
        "value": "health wellbeing improved"
    },
    {
        "value": "activity including participation"
    },
    {
        "value": "better collective understanding"
    },
    {
        "value": "context preservation historical"
    },
    {
        "value": "development namely child"
    },
    {
        "value": "feeling reduced"
    },
    {
        "value": "improve people health"
    },
    {
        "value": "heritage preservation backdrop"
    },
    {
        "value": "development event industry"
    },
    {
        "value": "sense civic"
    },
    {
        "value": "urban architectural quality"
    },
    {
        "value": "support community development"
    },
    {
        "value": "cultural amenity planning"
    },
    {
        "value": "identity community"
    },
    {
        "value": "build community organizational"
    },
    {
        "value": "improving quality health"
    },
    {
        "value": "social bond likely"
    },
    {
        "value": "country support project"
    },
    {
        "value": "feeling enhanced confidence"
    },
    {
        "value": "sense wellbeing control"
    },
    {
        "value": "behavior sexual"
    },
    {
        "value": "stewardship one"
    },
    {
        "value": "community support group"
    },
    {
        "value": "place attachment make"
    },
    {
        "value": "sense personal wellbeing"
    },
    {
        "value": "discrimination oppression need"
    },
    {
        "value": "inward investment regional"
    },
    {
        "value": "activity participation combined"
    },
    {
        "value": "cultivate experience skill"
    },
    {
        "value": "social ethic"
    },
    {
        "value": "education economic sustainability"
    },
    {
        "value": "individual participation activity"
    },
    {
        "value": "relating preservation historic"
    },
    {
        "value": "people sense belonging"
    },
    {
        "value": "creation job positive"
    },
    {
        "value": "cultural amenity museum"
    },
    {
        "value": "community involvement project"
    },
    {
        "value": "creating new job"
    },
    {
        "value": "deeper understanding people"
    },
    {
        "value": "whose culture tradition"
    },
    {
        "value": "literature place attachment"
    },
    {
        "value": "cultural amenity neighborhood"
    },
    {
        "value": "develop creativity"
    },
    {
        "value": "educational impact child"
    },
    {
        "value": "help people extend"
    },
    {
        "value": "also social activity"
    },
    {
        "value": "project included community"
    },
    {
        "value": "build existing organizational"
    },
    {
        "value": "self esteem higher"
    },
    {
        "value": "project historic preservation"
    },
    {
        "value": "expectation discrimination"
    },
    {
        "value": "profound influence people"
    },
    {
        "value": "attracts inward investment"
    },
    {
        "value": "design urban planning"
    },
    {
        "value": "foundation industry development"
    },
    {
        "value": "social bond group"
    },
    {
        "value": "place attachment local"
    },
    {
        "value": "preservation history"
    },
    {
        "value": "improved ability accurately"
    },
    {
        "value": "increased social activity"
    },
    {
        "value": "community center project"
    },
    {
        "value": "cultural amenity contingent"
    },
    {
        "value": "cultural amenity employer"
    },
    {
        "value": "social capital could"
    },
    {
        "value": "depression could reduced"
    },
    {
        "value": "clustering creative industry"
    },
    {
        "value": "historic building heritage"
    },
    {
        "value": "community project last"
    },
    {
        "value": "wellbeing improve"
    },
    {
        "value": "stimulating job creation"
    },
    {
        "value": "historical preservation"
    },
    {
        "value": "competitiveness aspect improved"
    },
    {
        "value": "cultural heritage archival"
    },
    {
        "value": "addiction drug"
    },
    {
        "value": "help art career"
    },
    {
        "value": "increased feeling confidence"
    },
    {
        "value": "problem gentrification"
    },
    {
        "value": "lower self esteem"
    },
    {
        "value": "project support"
    },
    {
        "value": "people develop creative"
    },
    {
        "value": "personal confidence"
    },
    {
        "value": "trajectory sexual behavior"
    },
    {
        "value": "life quality people"
    },
    {
        "value": "significantly reduced depression"
    },
    {
        "value": "connected heritage preservation"
    },
    {
        "value": "cluster creative business"
    },
    {
        "value": "tradition new town"
    },
    {
        "value": "child development"
    },
    {
        "value": "local development culture"
    },
    {
        "value": "reactive drug addiction"
    },
    {
        "value": "think socialize"
    },
    {
        "value": "strong sense place"
    },
    {
        "value": "social sustainability green"
    },
    {
        "value": "joy sadness happiness"
    },
    {
        "value": "anxiety feeling enhanced"
    },
    {
        "value": "city repositioning"
    },
    {
        "value": "ability improved"
    },
    {
        "value": "project individual support"
    },
    {
        "value": "development child"
    },
    {
        "value": "people certain influence"
    },
    {
        "value": "good poor health"
    },
    {
        "value": "economic social capital"
    },
    {
        "value": "part community project"
    },
    {
        "value": "non discrimination equality"
    },
    {
        "value": "job creation cultural"
    },
    {
        "value": "cultural leisure facility"
    },
    {
        "value": "community capacity building"
    },
    {
        "value": "child educational performance"
    },
    {
        "value": "benefit gentrification"
    },
    {
        "value": "people try influence"
    },
    {
        "value": "bond social"
    },
    {
        "value": "community bond"
    },
    {
        "value": "historical cultural preservation"
    },
    {
        "value": "culture well tradition"
    },
    {
        "value": "effective public consultation"
    },
    {
        "value": "attuned ability communicate"
    },
    {
        "value": "sense place enhanced"
    },
    {
        "value": "understanding diversity something"
    },
    {
        "value": "improved overall sense"
    },
    {
        "value": "sexual behavior child"
    },
    {
        "value": "feeling depression anxiety"
    },
    {
        "value": "cultural amenity may"
    },
    {
        "value": "process job creation"
    },
    {
        "value": "industry industry development"
    },
    {
        "value": "drug addiction"
    },
    {
        "value": "addition community project"
    },
    {
        "value": "creativity help"
    },
    {
        "value": "support community"
    },
    {
        "value": "discrimination extreme"
    },
    {
        "value": "right discrimination"
    },
    {
        "value": "people quality"
    },
    {
        "value": "ecological sustainability also"
    },
    {
        "value": "free sexual behavior"
    },
    {
        "value": "project focus community"
    },
    {
        "value": "stewardship type"
    },
    {
        "value": "job creation several"
    },
    {
        "value": "increased confidence motivation"
    },
    {
        "value": "industry development designed"
    },
    {
        "value": "industry development within"
    },
    {
        "value": "achieved development partnership"
    },
    {
        "value": "environmental social sustainability"
    },
    {
        "value": "cultural amenity community"
    },
    {
        "value": "training opportunity took"
    },
    {
        "value": "aesthetic historical heritage"
    },
    {
        "value": "growth risk gentrification"
    },
    {
        "value": "promote intercultural understanding"
    },
    {
        "value": "identity place attachment"
    },
    {
        "value": "social capital lesser"
    },
    {
        "value": "facilitate development project"
    },
    {
        "value": "development partnership formal"
    },
    {
        "value": "new technology development"
    },
    {
        "value": "get people feel"
    },
    {
        "value": "gentrification consequently"
    },
    {
        "value": "inward investment urban"
    },
    {
        "value": "accessible cultural amenity"
    },
    {
        "value": "involvement social"
    },
    {
        "value": "support development project"
    },
    {
        "value": "leisure facility retail"
    },
    {
        "value": "discrimination racism"
    },
    {
        "value": "new leisure"
    },
    {
        "value": "social participation greater"
    },
    {
        "value": "feel better go"
    },
    {
        "value": "political reality discrimination"
    },
    {
        "value": "participation activity"
    },
    {
        "value": "element healthier lifestyle"
    },
    {
        "value": "repositioning city"
    },
    {
        "value": "community cooperation networking"
    },
    {
        "value": "wellbeing improved time"
    },
    {
        "value": "social sustainability welfare"
    },
    {
        "value": "feeling solidarity"
    },
    {
        "value": "racial discrimination simply"
    },
    {
        "value": "education adult development"
    },
    {
        "value": "core attraction tourism"
    },
    {
        "value": "place attachment increased"
    },
    {
        "value": "cultural amenity coastal"
    },
    {
        "value": "opportunity training"
    },
    {
        "value": "contributes creation job"
    },
    {
        "value": "well social bond"
    },
    {
        "value": "social capital strengthening"
    },
    {
        "value": "job creation potential"
    },
    {
        "value": "fsa reduced anxiety"
    },
    {
        "value": "skill go develop"
    },
    {
        "value": "social activity total"
    },
    {
        "value": "pain depression reduced"
    },
    {
        "value": "participation kind activity"
    },
    {
        "value": "preserving heritage building"
    },
    {
        "value": "happiness joy contentment"
    },
    {
        "value": "within community project"
    },
    {
        "value": "feeling lack confidence"
    },
    {
        "value": "development work child"
    },
    {
        "value": "make feel better"
    },
    {
        "value": "people accept risk"
    },
    {
        "value": "quality architecture urban"
    },
    {
        "value": "experience needed work"
    },
    {
        "value": "technology development new"
    },
    {
        "value": "management project support"
    },
    {
        "value": "new project community"
    },
    {
        "value": "creative industry cluster"
    },
    {
        "value": "better understanding diverse"
    },
    {
        "value": "city heritage preservation"
    },
    {
        "value": "starting alcohol intake"
    },
    {
        "value": "racism discrimination oppressive"
    },
    {
        "value": "support education opportunity"
    },
    {
        "value": "drug caused addiction"
    },
    {
        "value": "improving quality life"
    },
    {
        "value": "symptom wellbeing improved"
    },
    {
        "value": "social activity although"
    },
    {
        "value": "improved emotional wellbeing"
    },
    {
        "value": "reality discrimination marginalization"
    },
    {
        "value": "historical heritage"
    },
    {
        "value": "inward investment city"
    },
    {
        "value": "support major project"
    },
    {
        "value": "approach industry development"
    },
    {
        "value": "economic sustainability social"
    },
    {
        "value": "ability improved ability"
    },
    {
        "value": "time poor health"
    },
    {
        "value": "violence prejudice discrimination"
    },
    {
        "value": "stimulate interest confidence"
    },
    {
        "value": "skill create work"
    },
    {
        "value": "healthier lifestyle"
    },
    {
        "value": "child development human"
    },
    {
        "value": "sense better understanding"
    },
    {
        "value": "educational development"
    },
    {
        "value": "cultural activity participation"
    },
    {
        "value": "influence many others"
    },
    {
        "value": "sense wellbeing like"
    },
    {
        "value": "enhanced feeling confidence"
    },
    {
        "value": "anxiety reduced"
    },
    {
        "value": "activity participation corresponding"
    },
    {
        "value": "talent local cultural"
    },
    {
        "value": "attachment community"
    },
    {
        "value": "live make comfortable"
    },
    {
        "value": "drug addiction however"
    },
    {
        "value": "planning urban design"
    },
    {
        "value": "give sense wellbeing"
    },
    {
        "value": "local talent local"
    },
    {
        "value": "term job creation"
    },
    {
        "value": "activity economic participation"
    },
    {
        "value": "civic participation activity"
    },
    {
        "value": "social capital including"
    },
    {
        "value": "social bond improving"
    },
    {
        "value": "discrimination cultural exclusion"
    },
    {
        "value": "sense wellbeing good"
    },
    {
        "value": "preservation heritage experience"
    },
    {
        "value": "model social sustainability"
    },
    {
        "value": "actually feel better"
    },
    {
        "value": "attachment place pointing"
    },
    {
        "value": "sustainability local social"
    },
    {
        "value": "better quality life"
    },
    {
        "value": "feeling depression long"
    },
    {
        "value": "boost productivity competitiveness"
    },
    {
        "value": "gentrification esteban"
    },
    {
        "value": "contribute conflict resolution"
    },
    {
        "value": "development sustainability social"
    },
    {
        "value": "stop alcohol intake"
    },
    {
        "value": "person feel better"
    },
    {
        "value": "historic heritage building"
    },
    {
        "value": "stewardship particular"
    },
    {
        "value": "preservation historical value"
    },
    {
        "value": "sustainability social wellbeing"
    },
    {
        "value": "cultural amenity investment"
    },
    {
        "value": "use new skill"
    },
    {
        "value": "simultaneously development partnership"
    },
    {
        "value": "create local identity"
    },
    {
        "value": "depression increased feeling"
    },
    {
        "value": "local culture heritage"
    },
    {
        "value": "improve life people"
    },
    {
        "value": "increased social connec"
    },
    {
        "value": "involved environmental improvement"
    },
    {
        "value": "identity strengthen local"
    },
    {
        "value": "pleasure joy happiness"
    },
    {
        "value": "new community project"
    },
    {
        "value": "culture enhance pride"
    },
    {
        "value": "signicantly reduced feeling"
    },
    {
        "value": "community support network"
    },
    {
        "value": "intake alcohol indirectly"
    },
    {
        "value": "reduced anxiety level"
    },
    {
        "value": "community original project"
    },
    {
        "value": "mood diminished anxiety"
    },
    {
        "value": "training opportunity help"
    },
    {
        "value": "others ability communicate"
    },
    {
        "value": "quality life good"
    },
    {
        "value": "recovery addiction drug"
    },
    {
        "value": "environmental economic sustainability"
    },
    {
        "value": "gentrification justificatory"
    },
    {
        "value": "healthier active lifestyle"
    },
    {
        "value": "part local identity"
    },
    {
        "value": "social capital likely"
    },
    {
        "value": "people influence"
    },
    {
        "value": "place attachment level"
    },
    {
        "value": "social participation lower"
    },
    {
        "value": "happiness joy"
    },
    {
        "value": "better self esteem"
    },
    {
        "value": "developing people creativity"
    },
    {
        "value": "sense community project"
    },
    {
        "value": "community project four"
    },
    {
        "value": "improve overall wellbeing"
    },
    {
        "value": "historical heritage developing"
    },
    {
        "value": "social capital"
    },
    {
        "value": "depression symptom reduced"
    },
    {
        "value": "confidence culture"
    },
    {
        "value": "discrimination policy"
    },
    {
        "value": "build community support"
    },
    {
        "value": "community based project"
    },
    {
        "value": "project including community"
    },
    {
        "value": "pride culture tradition"
    },
    {
        "value": "increased quality life"
    },
    {
        "value": "increased selfesteem confidence"
    },
    {
        "value": "developed ability communicate"
    },
    {
        "value": "also improved ability"
    },
    {
        "value": "drug addiction also"
    },
    {
        "value": "medium gentrification gentrification"
    },
    {
        "value": "increased social capital"
    },
    {
        "value": "historic preservation area"
    },
    {
        "value": "depression diminished"
    },
    {
        "value": "social sustainability system"
    },
    {
        "value": "tourism inward investment"
    },
    {
        "value": "alcohol intake nevertheless"
    },
    {
        "value": "environmental sustainability economic"
    },
    {
        "value": "center social sustainability"
    },
    {
        "value": "job creation strength"
    },
    {
        "value": "sense improved well"
    },
    {
        "value": "preservation cultural artefact"
    },
    {
        "value": "social capital increase"
    },
    {
        "value": "activity participation improved"
    },
    {
        "value": "show project community"
    },
    {
        "value": "social sustainability value"
    },
    {
        "value": "social activity"
    },
    {
        "value": "project also support"
    },
    {
        "value": "joy happiness enjoyment"
    },
    {
        "value": "downtown amenity cultural"
    },
    {
        "value": "offender victim address"
    },
    {
        "value": "cultural entertainment amenity"
    },
    {
        "value": "diminished anxiety"
    },
    {
        "value": "industry new technology"
    },
    {
        "value": "top development industry"
    },
    {
        "value": "marketing urban"
    },
    {
        "value": "capacity community improve"
    },
    {
        "value": "reduced depression symptom"
    },
    {
        "value": "social activity level"
    },
    {
        "value": "cultural amenity agglomeration"
    },
    {
        "value": "people control life"
    },
    {
        "value": "responsiveness public service"
    },
    {
        "value": "child educational"
    },
    {
        "value": "effect tourism attraction"
    },
    {
        "value": "attachment place often"
    },
    {
        "value": "importance place attachment"
    },
    {
        "value": "preservation heritage"
    },
    {
        "value": "educational attainment child"
    },
    {
        "value": "community support organization"
    },
    {
        "value": "around cultural amenity"
    },
    {
        "value": "reduced feeling stress"
    },
    {
        "value": "project turn community"
    },
    {
        "value": "increased ability communicate"
    },
    {
        "value": "little place attachment"
    },
    {
        "value": "called community project"
    },
    {
        "value": "like social capital"
    },
    {
        "value": "visitor inward investment"
    },
    {
        "value": "urban quality"
    },
    {
        "value": "way develop creativity"
    },
    {
        "value": "improved health many"
    },
    {
        "value": "conventional service delivery"
    },
    {
        "value": "people employability help"
    },
    {
        "value": "heritage historical"
    },
    {
        "value": "local culture tradition"
    },
    {
        "value": "effort support project"
    },
    {
        "value": "city image strategy"
    },
    {
        "value": "anxiety reduced post"
    },
    {
        "value": "understanding drug addiction"
    },
    {
        "value": "drug addiction among"
    },
    {
        "value": "community involvement activity"
    },
    {
        "value": "facilitate collaboration"
    },
    {
        "value": "bond community"
    },
    {
        "value": "mean improving wellbeing"
    },
    {
        "value": "financial economic sustainability"
    },
    {
        "value": "development framework partnership"
    },
    {
        "value": "calmness reduced anxiety"
    },
    {
        "value": "support local project"
    },
    {
        "value": "drug addiction raise"
    },
    {
        "value": "satisfaction place attachment"
    },
    {
        "value": "political activity"
    },
    {
        "value": "stewardship also"
    },
    {
        "value": "aspect ecological sustainability"
    },
    {
        "value": "local quality life"
    },
    {
        "value": "activity participation"
    },
    {
        "value": "market job creation"
    },
    {
        "value": "people feel like"
    },
    {
        "value": "better understanding nature"
    },
    {
        "value": "back heritage historical"
    },
    {
        "value": "availability cultural amenity"
    },
    {
        "value": "cultural amenity including"
    },
    {
        "value": "educational many child"
    },
    {
        "value": "treatment drug addiction"
    },
    {
        "value": "increased feeling wellbeing"
    },
    {
        "value": "family improved quality"
    },
    {
        "value": "tourist growth inflow"
    },
    {
        "value": "identity local"
    },
    {
        "value": "reduced pain anxiety"
    },
    {
        "value": "opinion want opinion"
    },
    {
        "value": "ecology sustainability"
    },
    {
        "value": "discrimination social"
    },
    {
        "value": "education training opportunity"
    },
    {
        "value": "strengthen capacity community"
    },
    {
        "value": "social side sustainability"
    },
    {
        "value": "better level diversity"
    },
    {
        "value": "increase participation social"
    },
    {
        "value": "socialize people help"
    },
    {
        "value": "participating community project"
    },
    {
        "value": "tradition culture help"
    },
    {
        "value": "community community project"
    },
    {
        "value": "like live make"
    },
    {
        "value": "future support community"
    },
    {
        "value": "however atmosphere relaxed"
    },
    {
        "value": "residence cultural amenity"
    },
    {
        "value": "reduced anxiety seven"
    },
    {
        "value": "continuing participation activity"
    },
    {
        "value": "heritage preserve"
    },
    {
        "value": "associated cultural amenity"
    },
    {
        "value": "local identity"
    },
    {
        "value": "feeling anxiety regarding"
    },
    {
        "value": "participation increase social"
    },
    {
        "value": "wellbeing significantly improved"
    },
    {
        "value": "project small community"
    },
    {
        "value": "wellbeing brought improved"
    },
    {
        "value": "live feel"
    },
    {
        "value": "activity cultural participation"
    },
    {
        "value": "improving competitiveness"
    },
    {
        "value": "divide cultural amenity"
    },
    {
        "value": "also industry development"
    },
    {
        "value": "effective public participation"
    },
    {
        "value": "talk discrimination oppression"
    },
    {
        "value": "condition job creation"
    },
    {
        "value": "sense identity enhanced"
    },
    {
        "value": "social capital one"
    },
    {
        "value": "self esteem increase"
    },
    {
        "value": "people better make"
    },
    {
        "value": "involvement environmental improvement"
    },
    {
        "value": "sense increased"
    },
    {
        "value": "good social ethic"
    },
    {
        "value": "access cultural amenity"
    },
    {
        "value": "ability communicate effectively"
    },
    {
        "value": "development industry"
    },
    {
        "value": "developed community network"
    },
    {
        "value": "systemic racism discrimination"
    },
    {
        "value": "local project community"
    },
    {
        "value": "sense place better"
    },
    {
        "value": "increased sense local"
    },
    {
        "value": "project member community"
    },
    {
        "value": "thought feeling depression"
    },
    {
        "value": "social bond cultural"
    },
    {
        "value": "city economic sustainability"
    },
    {
        "value": "preservation old heritage"
    },
    {
        "value": "tradition local community"
    },
    {
        "value": "discrimination marginalization"
    },
    {
        "value": "historical preservation national"
    },
    {
        "value": "identity enhanced social"
    },
    {
        "value": "decrease feeling stress"
    },
    {
        "value": "participation new activity"
    },
    {
        "value": "greater social capital"
    },
    {
        "value": "community project community"
    },
    {
        "value": "cultural participation activity"
    },
    {
        "value": "sense wellbeing see"
    },
    {
        "value": "project plus community"
    },
    {
        "value": "social capital social"
    },
    {
        "value": "culture tradition region"
    },
    {
        "value": "better understanding participatory"
    },
    {
        "value": "reduced stress anxiety"
    },
    {
        "value": "cultural tradition heritage"
    },
    {
        "value": "support group community"
    },
    {
        "value": "way improve wellbeing"
    },
    {
        "value": "project work support"
    },
    {
        "value": "social ethic policy"
    },
    {
        "value": "distinction consumer creator"
    },
    {
        "value": "leisure facility service"
    },
    {
        "value": "cultural heritage preservation"
    },
    {
        "value": "inward investment"
    },
    {
        "value": "eventual drug addiction"
    },
    {
        "value": "community several project"
    },
    {
        "value": "job creation place"
    },
    {
        "value": "social capital significantly"
    },
    {
        "value": "job creation export"
    },
    {
        "value": "leisure facility"
    },
    {
        "value": "social sustainability see"
    },
    {
        "value": "discrimination although"
    },
    {
        "value": "social capital four"
    },
    {
        "value": "transform responsiveness public"
    },
    {
        "value": "decreased participation activity"
    },
    {
        "value": "support network community"
    },
    {
        "value": "activity participation improve"
    },
    {
        "value": "use development industry"
    },
    {
        "value": "facilitate public consultation"
    },
    {
        "value": "wellbeing developing sense"
    },
    {
        "value": "capital well social"
    },
    {
        "value": "others make feel"
    },
    {
        "value": "development child civic"
    },
    {
        "value": "involved process regeneration"
    },
    {
        "value": "social bond building"
    },
    {
        "value": "development industry commerce"
    },
    {
        "value": "community project take"
    },
    {
        "value": "support community participation"
    },
    {
        "value": "cultural natural amenity"
    },
    {
        "value": "involvement community activity"
    },
    {
        "value": "improved health life"
    },
    {
        "value": "influence others"
    },
    {
        "value": "better understanding current"
    },
    {
        "value": "cultural amenity classic"
    },
    {
        "value": "reduced anxiety fatigue"
    },
    {
        "value": "reduced feeling"
    },
    {
        "value": "discrimination marginalization legacy"
    },
    {
        "value": "economic growth sustainability"
    },
    {
        "value": "relate feeling depression"
    },
    {
        "value": "improving people life"
    },
    {
        "value": "improved quality urban"
    },
    {
        "value": "depression increased sense"
    },
    {
        "value": "help stimulate creativity"
    },
    {
        "value": "higher self esteem"
    },
    {
        "value": "regional job creation"
    },
    {
        "value": "reinforcing local identity"
    },
    {
        "value": "identity enhance"
    },
    {
        "value": "commitment healthier lifestyle"
    },
    {
        "value": "strengthen social bond"
    },
    {
        "value": "confidence definitely increased"
    },
    {
        "value": "tradition value culture"
    },
    {
        "value": "offer cultural amenity"
    },
    {
        "value": "feeling well reduced"
    },
    {
        "value": "development smart industry"
    },
    {
        "value": "positively influence people"
    },
    {
        "value": "distress improved wellbeing"
    },
    {
        "value": "volunteer involve regeneration"
    },
    {
        "value": "industry art development"
    },
    {
        "value": "experience help develop"
    },
    {
        "value": "social capital however"
    },
    {
        "value": "feeling stigmatized anxiety"
    },
    {
        "value": "nicer make feel"
    },
    {
        "value": "implication right discrimination"
    },
    {
        "value": "increased pain anxiety"
    },
    {
        "value": "better overall understanding"
    },
    {
        "value": "know people feel"
    },
    {
        "value": "provide route rehabilitation"
    },
    {
        "value": "drug alcohol addiction"
    },
    {
        "value": "associated happiness joy"
    },
    {
        "value": "physical activity participation"
    },
    {
        "value": "social sustainability urban"
    },
    {
        "value": "social bond new"
    },
    {
        "value": "result social capital"
    },
    {
        "value": "life poor"
    },
    {
        "value": "production preservation historical"
    },
    {
        "value": "development industry result"
    },
    {
        "value": "exposure racism discrimination"
    },
    {
        "value": "skill help"
    },
    {
        "value": "activity although social"
    },
    {
        "value": "job creation b"
    },
    {
        "value": "industry development policy"
    },
    {
        "value": "heritage preservation traditional"
    },
    {
        "value": "support child development"
    },
    {
        "value": "heritage saida historic"
    },
    {
        "value": "image city"
    },
    {
        "value": "experience build"
    },
    {
        "value": "concept social sustainability"
    },
    {
        "value": "route rehabilitation integration"
    },
    {
        "value": "improved wellbeing result"
    },
    {
        "value": "feel better live"
    },
    {
        "value": "confidence increased"
    },
    {
        "value": "poor quality living"
    },
    {
        "value": "community project provide"
    },
    {
        "value": "understanding heritage preservation"
    },
    {
        "value": "development impact partnership"
    },
    {
        "value": "access education health"
    },
    {
        "value": "community participation activity"
    },
    {
        "value": "community research project"
    },
    {
        "value": "community increasing sense"
    },
    {
        "value": "gain community cooperation"
    },
    {
        "value": "discrimination acceptance"
    },
    {
        "value": "gentrification gentrification"
    },
    {
        "value": "heritage preservation making"
    },
    {
        "value": "cultural amenity user"
    },
    {
        "value": "encourage training opportunity"
    },
    {
        "value": "cultural amenity usually"
    },
    {
        "value": "perception place attachment"
    },
    {
        "value": "decline social capital"
    },
    {
        "value": "depression increasing feeling"
    },
    {
        "value": "sexual behavior"
    },
    {
        "value": "industry development needed"
    },
    {
        "value": "discrimination exclusion"
    },
    {
        "value": "people know better"
    },
    {
        "value": "increased selfconfidence wellbeing"
    },
    {
        "value": "civic support project"
    },
    {
        "value": "job creation could"
    },
    {
        "value": "nature new amenity"
    },
    {
        "value": "general sense wellbeing"
    },
    {
        "value": "moreover social capital"
    },
    {
        "value": "culture tradition cultural"
    },
    {
        "value": "consequence gentrification"
    },
    {
        "value": "project community led"
    },
    {
        "value": "heritage museum historic"
    },
    {
        "value": "see place attachment"
    },
    {
        "value": "discrimination prejudice"
    },
    {
        "value": "development project community"
    },
    {
        "value": "sexual behavior particularly"
    },
    {
        "value": "people feel sense"
    },
    {
        "value": "social capital improved"
    },
    {
        "value": "much activity participation"
    },
    {
        "value": "without discrimination exclusion"
    },
    {
        "value": "sense health wellbeing"
    },
    {
        "value": "discrimination oppressive"
    },
    {
        "value": "historical artistic heritage"
    },
    {
        "value": "place attachment satisfaction"
    },
    {
        "value": "reducing depression anxiety"
    },
    {
        "value": "community development support"
    },
    {
        "value": "tangible identity enhanced"
    },
    {
        "value": "related social capital"
    },
    {
        "value": "social capital three"
    },
    {
        "value": "historic preservation site"
    },
    {
        "value": "good urban design"
    },
    {
        "value": "wellbeing improved equally"
    },
    {
        "value": "another better understanding"
    },
    {
        "value": "interaction communal meaning"
    },
    {
        "value": "economic social sustainability"
    },
    {
        "value": "feeling depression youth"
    },
    {
        "value": "promote happiness joy"
    },
    {
        "value": "help body image"
    },
    {
        "value": "strengthening intercultural contact"
    },
    {
        "value": "job creation property"
    },
    {
        "value": "social capital deeper"
    },
    {
        "value": "feeling increased"
    },
    {
        "value": "control life people"
    },
    {
        "value": "surrounding industry development"
    },
    {
        "value": "improved health"
    },
    {
        "value": "project based community"
    },
    {
        "value": "cultural amenity hailed"
    },
    {
        "value": "including community project"
    },
    {
        "value": "influence people whether"
    },
    {
        "value": "gentrification also"
    },
    {
        "value": "cultural amenity also"
    },
    {
        "value": "increased social"
    },
    {
        "value": "community deliver project"
    },
    {
        "value": "industry development level"
    },
    {
        "value": "also preservation cultural"
    },
    {
        "value": "make feel really"
    },
    {
        "value": "health participation activity"
    },
    {
        "value": "building community capacity"
    },
    {
        "value": "increased social bond"
    },
    {
        "value": "normally socialize"
    },
    {
        "value": "feeling confidence"
    },
    {
        "value": "government social capital"
    },
    {
        "value": "sense overall wellbeing"
    },
    {
        "value": "growth job creation"
    },
    {
        "value": "people develop community"
    },
    {
        "value": "activity regular participation"
    },
    {
        "value": "activity involvement"
    },
    {
        "value": "amenity unique cultural"
    },
    {
        "value": "discrimination characterizes"
    },
    {
        "value": "abuse discrimination"
    },
    {
        "value": "relaxed atmosphere health"
    },
    {
        "value": "social sustainability supporting"
    },
    {
        "value": "tourism attraction even"
    },
    {
        "value": "heritage historical building"
    },
    {
        "value": "child adolescent development"
    },
    {
        "value": "building tourism attraction"
    },
    {
        "value": "impact identity awareness"
    },
    {
        "value": "improving wellbeing"
    },
    {
        "value": "feeling helplessness depression"
    },
    {
        "value": "better socializing"
    },
    {
        "value": "strengthening competitiveness"
    },
    {
        "value": "cultural amenity spatial"
    },
    {
        "value": "industry development program"
    },
    {
        "value": "heritage culture tradition"
    },
    {
        "value": "intercultural relationship"
    },
    {
        "value": "activity total social"
    },
    {
        "value": "project support social"
    },
    {
        "value": "anxiety feeling"
    },
    {
        "value": "increased sense community"
    },
    {
        "value": "feeling relieving anxiety"
    },
    {
        "value": "relief feeling anxiety"
    },
    {
        "value": "quality urban"
    },
    {
        "value": "research project community"
    },
    {
        "value": "offering cultural amenity"
    },
    {
        "value": "tradition cultural heritage"
    },
    {
        "value": "facility leisure activity"
    },
    {
        "value": "planning design urban"
    },
    {
        "value": "improved urban"
    },
    {
        "value": "cultural amenity approach"
    },
    {
        "value": "tourist inward investment"
    },
    {
        "value": "people mention influence"
    },
    {
        "value": "community project elsewhere"
    },
    {
        "value": "community development supporting"
    },
    {
        "value": "natural cultural amenity"
    },
    {
        "value": "ability produce communicate"
    },
    {
        "value": "people regeneration process"
    },
    {
        "value": "participation local activity"
    },
    {
        "value": "history heritage conservation"
    },
    {
        "value": "development industry see"
    },
    {
        "value": "activity participation perceived"
    },
    {
        "value": "making people feel"
    },
    {
        "value": "participation community support"
    },
    {
        "value": "ability improve"
    },
    {
        "value": "leisure new"
    },
    {
        "value": "enhance competitiveness"
    },
    {
        "value": "socialize really"
    },
    {
        "value": "industry development effectively"
    },
    {
        "value": "community group support"
    },
    {
        "value": "take training education"
    },
    {
        "value": "economic sustainability strong"
    },
    {
        "value": "meaning inclusive communal"
    },
    {
        "value": "participation social activity"
    },
    {
        "value": "social capital significant"
    },
    {
        "value": "project international community"
    },
    {
        "value": "new leisure area"
    },
    {
        "value": "retail leisure facility"
    },
    {
        "value": "creative industry development"
    },
    {
        "value": "challenge mep delivery"
    },
    {
        "value": "culture tradition"
    },
    {
        "value": "feeling stress decreased"
    },
    {
        "value": "sense community increasing"
    },
    {
        "value": "contribution community project"
    },
    {
        "value": "reality discrimination"
    },
    {
        "value": "project support group"
    },
    {
        "value": "attachment place continuously"
    },
    {
        "value": "far improved wellbeing"
    },
    {
        "value": "increase sense community"
    },
    {
        "value": "certain danger gentrification"
    },
    {
        "value": "job creation generation"
    },
    {
        "value": "historical cultural heritage"
    },
    {
        "value": "people think live"
    },
    {
        "value": "lead improved wellbeing"
    },
    {
        "value": "community run project"
    },
    {
        "value": "increasing sense belonging"
    },
    {
        "value": "participation physical activity"
    },
    {
        "value": "support community mission"
    },
    {
        "value": "understanding complexity diversity"
    },
    {
        "value": "support community effort"
    },
    {
        "value": "local identity even"
    },
    {
        "value": "social sustainability seem"
    },
    {
        "value": "international project community"
    },
    {
        "value": "additional activity social"
    },
    {
        "value": "project strengthen community"
    },
    {
        "value": "community project led"
    },
    {
        "value": "activity increased participation"
    },
    {
        "value": "sense wellbeing made"
    },
    {
        "value": "improved health wellbeing"
    },
    {
        "value": "facilitate development"
    },
    {
        "value": "job creation investment"
    },
    {
        "value": "involved community project"
    },
    {
        "value": "community support"
    },
    {
        "value": "tourism attraction new"
    },
    {
        "value": "job creation direct"
    },
    {
        "value": "increased self esteem"
    },
    {
        "value": "better understanding world"
    },
    {
        "value": "respect others opinion"
    },
    {
        "value": "activity increased social"
    },
    {
        "value": "urban design quality"
    },
    {
        "value": "industry community development"
    },
    {
        "value": "education social capital"
    },
    {
        "value": "place attachment social"
    },
    {
        "value": "literacy development child"
    },
    {
        "value": "cultural amenity easily"
    },
    {
        "value": "reduced level depression"
    },
    {
        "value": "life reduced depression"
    },
    {
        "value": "community commercial project"
    },
    {
        "value": "take education training"
    },
    {
        "value": "drug addiction work"
    },
    {
        "value": "child oriented educational"
    },
    {
        "value": "people feel little"
    },
    {
        "value": "child development social"
    },
    {
        "value": "change discrimination wake"
    },
    {
        "value": "self reliance project"
    },
    {
        "value": "social capital expected"
    },
    {
        "value": "improved wellbeing self"
    },
    {
        "value": "social bond improve"
    },
    {
        "value": "transformation city image"
    },
    {
        "value": "social capital much"
    },
    {
        "value": "heritage historical root"
    },
    {
        "value": "people develop creativity"
    },
    {
        "value": "participation increased"
    },
    {
        "value": "social cultural sustainability"
    },
    {
        "value": "improved urban management"
    },
    {
        "value": "improving people health"
    },
    {
        "value": "activity extended"
    },
    {
        "value": "point discrimination"
    },
    {
        "value": "sense involvement people"
    },
    {
        "value": "struggling feeling depression"
    },
    {
        "value": "consider encourage people"
    },
    {
        "value": "community project member"
    },
    {
        "value": "social capital added"
    },
    {
        "value": "social amenity"
    },
    {
        "value": "educational development child"
    },
    {
        "value": "sustainability social"
    },
    {
        "value": "joy happiness"
    },
    {
        "value": "grant support project"
    },
    {
        "value": "increase self esteem"
    },
    {
        "value": "problem heritage preservation"
    },
    {
        "value": "feeling anxiety experiencing"
    },
    {
        "value": "drug addiction biopsychosocial"
    },
    {
        "value": "potential gentrification"
    },
    {
        "value": "health poor"
    },
    {
        "value": "attraction tourism city"
    },
    {
        "value": "attachment place identity"
    },
    {
        "value": "special attachment place"
    },
    {
        "value": "spend job creation"
    },
    {
        "value": "raise vision beyond"
    },
    {
        "value": "social community bond"
    },
    {
        "value": "new headquarters leisure"
    },
    {
        "value": "social capital increased"
    },
    {
        "value": "social bond across"
    },
    {
        "value": "cultural social bond"
    },
    {
        "value": "heritage preservation project"
    },
    {
        "value": "regeneration process involved"
    },
    {
        "value": "local self reliance"
    },
    {
        "value": "skill work experience"
    },
    {
        "value": "food alcohol intake"
    },
    {
        "value": "city image branding"
    },
    {
        "value": "variety community project"
    },
    {
        "value": "development new business"
    },
    {
        "value": "atmosphere health"
    },
    {
        "value": "create job"
    },
    {
        "value": "contact developed"
    },
    {
        "value": "capacity building community"
    },
    {
        "value": "job creation worth"
    },
    {
        "value": "community participation project"
    },
    {
        "value": "attract inward investment"
    },
    {
        "value": "creation job empowering"
    },
    {
        "value": "anxiety depression reduced"
    },
    {
        "value": "forum intercultural understanding"
    },
    {
        "value": "understanding diversity"
    },
    {
        "value": "qualified job creation"
    },
    {
        "value": "short ecological sustainability"
    },
    {
        "value": "improve body image"
    },
    {
        "value": "improving region competitiveness"
    },
    {
        "value": "time socialize"
    },
    {
        "value": "increased sense"
    },
    {
        "value": "larger industry development"
    },
    {
        "value": "making tourism attraction"
    },
    {
        "value": "social capital mainly"
    },
    {
        "value": "socialize well"
    },
    {
        "value": "violence sexism discrimination"
    },
    {
        "value": "strengthening social capital"
    },
    {
        "value": "cultural diversity amenity"
    },
    {
        "value": "attracting inward investment"
    },
    {
        "value": "improved wellbeing understanding"
    },
    {
        "value": "sense belonging community"
    },
    {
        "value": "victim address issue"
    },
    {
        "value": "sociability wellbeing improved"
    },
    {
        "value": "depression anxiety felt"
    },
    {
        "value": "atmosphere relaxed"
    },
    {
        "value": "increased community"
    },
    {
        "value": "place attachment place"
    },
    {
        "value": "danger gentrification possible"
    },
    {
        "value": "employment job creation"
    },
    {
        "value": "addiction drug created"
    },
    {
        "value": "drug addiction related"
    },
    {
        "value": "partnership develop"
    },
    {
        "value": "communal meaning social"
    },
    {
        "value": "community project project"
    },
    {
        "value": "social economic capital"
    },
    {
        "value": "gentrification hence"
    },
    {
        "value": "place attachment manifest"
    },
    {
        "value": "strengthened networking community"
    },
    {
        "value": "social sustainability via"
    },
    {
        "value": "reduced anxiety"
    },
    {
        "value": "right discrimination cultural"
    },
    {
        "value": "historic heritage"
    },
    {
        "value": "discrimination inequality believe"
    },
    {
        "value": "regeneration process facilitate"
    },
    {
        "value": "promotion job creation"
    },
    {
        "value": "social capital higher"
    },
    {
        "value": "diverse job creation"
    },
    {
        "value": "heritage historic"
    },
    {
        "value": "might support project"
    },
    {
        "value": "use sex behavior"
    },
    {
        "value": "inward investment place"
    },
    {
        "value": "leisure facility higher"
    },
    {
        "value": "important raise expectation"
    },
    {
        "value": "happiness joy enjoyment"
    },
    {
        "value": "skill develop"
    },
    {
        "value": "inappropriate social behavior"
    },
    {
        "value": "diversity intercultural understanding"
    },
    {
        "value": "improved quality health"
    },
    {
        "value": "alcohol intake unhealthy"
    },
    {
        "value": "attachment relation place"
    },
    {
        "value": "strengthen local identity"
    },
    {
        "value": "image public body"
    },
    {
        "value": "generation job creation"
    },
    {
        "value": "social capital may"
    },
    {
        "value": "people influence seen"
    },
    {
        "value": "development industry developed"
    },
    {
        "value": "social capital government"
    },
    {
        "value": "social capital mccarthy"
    },
    {
        "value": "help transform image"
    },
    {
        "value": "project support work"
    },
    {
        "value": "awareness one identity"
    },
    {
        "value": "risk gentrification exposure"
    },
    {
        "value": "social capital enhanced"
    },
    {
        "value": "force cultural amenity"
    },
    {
        "value": "building industry development"
    },
    {
        "value": "people live better"
    },
    {
        "value": "local support project"
    },
    {
        "value": "participation community activity"
    },
    {
        "value": "creating job"
    },
    {
        "value": "relationship cultural amenity"
    },
    {
        "value": "force discrimination"
    },
    {
        "value": "alcohol increased"
    },
    {
        "value": "increased confidence sense"
    },
    {
        "value": "preservation historic city"
    },
    {
        "value": "experience community project"
    },
    {
        "value": "addition drug addiction"
    },
    {
        "value": "project like community"
    },
    {
        "value": "feeling anxiety"
    },
    {
        "value": "community study support"
    },
    {
        "value": "job creation regional"
    },
    {
        "value": "sense wellbeing"
    },
    {
        "value": "influence place people"
    },
    {
        "value": "reduced symptom depression"
    },
    {
        "value": "declining social capital"
    },
    {
        "value": "preservation industrial heritage"
    },
    {
        "value": "form discrimination prejudice"
    },
    {
        "value": "available health education"
    },
    {
        "value": "leisure facility harvey"
    },
    {
        "value": "feeling increased selfconfidence"
    },
    {
        "value": "symptom alcohol intake"
    },
    {
        "value": "attended cultural amenity"
    },
    {
        "value": "industry new market"
    },
    {
        "value": "feel anxiety"
    },
    {
        "value": "issue feeling anxiety"
    },
    {
        "value": "industry development craft"
    },
    {
        "value": "new skill develop"
    },
    {
        "value": "place attachment joint"
    },
    {
        "value": "increased sense confidence"
    },
    {
        "value": "would support community"
    },
    {
        "value": "process support community"
    },
    {
        "value": "growing sense belonging"
    },
    {
        "value": "prejudice better understanding"
    },
    {
        "value": "total social activity"
    },
    {
        "value": "activity part social"
    },
    {
        "value": "community project also"
    },
    {
        "value": "project community go"
    },
    {
        "value": "infrastructure sustainability economic"
    },
    {
        "value": "facilitate consultation"
    },
    {
        "value": "local heritage preservation"
    },
    {
        "value": "activity including involvement"
    },
    {
        "value": "promote tolerance contribute"
    },
    {
        "value": "use facilitate development"
    },
    {
        "value": "job creation sustain"
    },
    {
        "value": "acceptance non discrimination"
    },
    {
        "value": "enhanced identity self"
    },
    {
        "value": "understanding better"
    },
    {
        "value": "depression reduced"
    },
    {
        "value": "heritage institution preservation"
    },
    {
        "value": "increased participation local"
    },
    {
        "value": "cultural amenity seven"
    },
    {
        "value": "stronger social bond"
    },
    {
        "value": "community particular project"
    },
    {
        "value": "area social sustainability"
    },
    {
        "value": "increased sense place"
    },
    {
        "value": "urban marketing"
    },
    {
        "value": "cultural participation increased"
    },
    {
        "value": "reduced anxiety young"
    },
    {
        "value": "insight social political"
    },
    {
        "value": "historic preservation"
    },
    {
        "value": "image branding city"
    },
    {
        "value": "self esteem low"
    },
    {
        "value": "social sustainability cultural"
    },
    {
        "value": "tourism attraction firm"
    },
    {
        "value": "sustainable development partnership"
    },
    {
        "value": "addiction drug fusion"
    },
    {
        "value": "improved planning design"
    },
    {
        "value": "identidad capital social"
    },
    {
        "value": "public voluntary sector"
    },
    {
        "value": "community benefitted project"
    },
    {
        "value": "better understanding"
    },
    {
        "value": "development robust partnership"
    },
    {
        "value": "sex behavior context"
    },
    {
        "value": "ability communicate"
    },
    {
        "value": "wellbeing enhanced sense"
    },
    {
        "value": "cultural amenity three"
    },
    {
        "value": "confidence stimulated"
    },
    {
        "value": "child intellectual development"
    },
    {
        "value": "activity social activity"
    },
    {
        "value": "also social capital"
    },
    {
        "value": "public participation activity"
    },
    {
        "value": "sexual risk behavior"
    },
    {
        "value": "facilitate effective public"
    },
    {
        "value": "impact gentrification"
    },
    {
        "value": "thus economic sustainability"
    },
    {
        "value": "decreasing sense wellbeing"
    },
    {
        "value": "people good make"
    },
    {
        "value": "social capital economic"
    },
    {
        "value": "effect attraction tourism"
    },
    {
        "value": "ecological sustainability culture"
    },
    {
        "value": "influence well people"
    },
    {
        "value": "found depression reduced"
    },
    {
        "value": "emotion joy happiness"
    },
    {
        "value": "discrimination acceptance violence"
    },
    {
        "value": "facilitate development group"
    },
    {
        "value": "showing job creation"
    },
    {
        "value": "know people live"
    },
    {
        "value": "employability help"
    },
    {
        "value": "headquarters leisure facility"
    },
    {
        "value": "true economic sustainability"
    },
    {
        "value": "economic sustainability urban"
    },
    {
        "value": "social bond community"
    },
    {
        "value": "identity enhanced"
    },
    {
        "value": "activity increasing involvement"
    },
    {
        "value": "gentrification time"
    },
    {
        "value": "ir cultural amenity"
    },
    {
        "value": "activity participation creation"
    },
    {
        "value": "help people feel"
    },
    {
        "value": "creativity people"
    },
    {
        "value": "resulting reduced anxiety"
    },
    {
        "value": "tolerance contribute conflict"
    },
    {
        "value": "gentrification gentrification urban"
    },
    {
        "value": "recognizes drug addiction"
    },
    {
        "value": "discrimination equality"
    },
    {
        "value": "new development"
    },
    {
        "value": "community project strengthen"
    },
    {
        "value": "time socialize well"
    },
    {
        "value": "cultural amenity diverse"
    },
    {
        "value": "higher social"
    },
    {
        "value": "contact generation help"
    },
    {
        "value": "exclusion discrimination aspect"
    },
    {
        "value": "creation job"
    },
    {
        "value": "enhancing historical heritage"
    },
    {
        "value": "develop partnership"
    },
    {
        "value": "improved quality life"
    },
    {
        "value": "sense wellbeing develop"
    },
    {
        "value": "development new"
    },
    {
        "value": "possibility gentrification"
    },
    {
        "value": "preservation historical building"
    },
    {
        "value": "support local community"
    },
    {
        "value": "quality life people"
    },
    {
        "value": "participation certain activity"
    },
    {
        "value": "depression reduced stress"
    },
    {
        "value": "heritage building heritage"
    },
    {
        "value": "communal meaning intrinsic"
    },
    {
        "value": "public service transforming"
    },
    {
        "value": "depression reduced large"
    },
    {
        "value": "part neighborhood community"
    },
    {
        "value": "type local identity"
    },
    {
        "value": "influence people life"
    },
    {
        "value": "cultural amenity catchment"
    },
    {
        "value": "ability effectively communicate"
    },
    {
        "value": "cultural preservation heritage"
    },
    {
        "value": "anxiety feel"
    },
    {
        "value": "involvement activity also"
    },
    {
        "value": "develop career art"
    },
    {
        "value": "community increased"
    },
    {
        "value": "new development innovation"
    },
    {
        "value": "art industry development"
    },
    {
        "value": "discrimination past"
    },
    {
        "value": "enhanced identity"
    },
    {
        "value": "therefore ability communicate"
    },
    {
        "value": "amenity cultural infrastructure"
    },
    {
        "value": "peer participation activity"
    },
    {
        "value": "behavior sex"
    },
    {
        "value": "important historical heritage"
    },
    {
        "value": "discrimination may"
    },
    {
        "value": "drug addiction performance"
    },
    {
        "value": "fundamental improved wellbeing"
    },
    {
        "value": "social capital also"
    },
    {
        "value": "network sociability"
    },
    {
        "value": "make people think"
    },
    {
        "value": "increased social cohesion"
    },
    {
        "value": "wellbeing improved experience"
    },
    {
        "value": "culture sustainability ecological"
    },
    {
        "value": "collaborative attitude"
    },
    {
        "value": "depression anxiety lower"
    },
    {
        "value": "communal meaning present"
    },
    {
        "value": "including historic heritage"
    },
    {
        "value": "advancing place attachment"
    },
    {
        "value": "network sociability promote"
    },
    {
        "value": "benefit community project"
    },
    {
        "value": "raise social capital"
    },
    {
        "value": "thinking cultural amenity"
    },
    {
        "value": "live somebody make"
    },
    {
        "value": "significantly reduced anxiety"
    },
    {
        "value": "sustainability economic impact"
    },
    {
        "value": "better understanding experience"
    },
    {
        "value": "together development industry"
    },
    {
        "value": "community attachment"
    },
    {
        "value": "better understanding people"
    },
    {
        "value": "influence people"
    },
    {
        "value": "child development learning"
    },
    {
        "value": "community would support"
    },
    {
        "value": "recreation facility leisure"
    },
    {
        "value": "alcohol intake stop"
    },
    {
        "value": "job created"
    },
    {
        "value": "social environmental sustainability"
    },
    {
        "value": "economic sustainability culture"
    },
    {
        "value": "address issue crime"
    },
    {
        "value": "promote better understanding"
    },
    {
        "value": "greater improvement wellbeing"
    },
    {
        "value": "industry development planning"
    },
    {
        "value": "confronting discrimination"
    },
    {
        "value": "calmed anxiety feeling"
    },
    {
        "value": "community project staff"
    },
    {
        "value": "prejudice discrimination"
    },
    {
        "value": "cultural amenity recognition"
    },
    {
        "value": "community town"
    },
    {
        "value": "partnership development"
    },
    {
        "value": "experience development partnership"
    },
    {
        "value": "design sustainability social"
    },
    {
        "value": "well social capital"
    },
    {
        "value": "participation activity participation"
    },
    {
        "value": "sense wellbeing one"
    },
    {
        "value": "social sustainability ecological"
    },
    {
        "value": "potentially improved wellbeing"
    },
    {
        "value": "reduction feeling depression"
    },
    {
        "value": "time confidence personal"
    },
    {
        "value": "place attachment intervention"
    },
    {
        "value": "training opportunity"
    },
    {
        "value": "community project put"
    },
    {
        "value": "improved sense well"
    },
    {
        "value": "job create"
    },
    {
        "value": "participating social activity"
    },
    {
        "value": "community project involved"
    },
    {
        "value": "understanding friendship"
    },
    {
        "value": "improving people quality"
    },
    {
        "value": "develop skill needed"
    },
    {
        "value": "heritage preservation historical"
    },
    {
        "value": "lower place attachment"
    },
    {
        "value": "increasing social capital"
    },
    {
        "value": "feeling depression"
    },
    {
        "value": "sense belonging involvement"
    },
    {
        "value": "place greater"
    },
    {
        "value": "job creation maintenance"
    },
    {
        "value": "joy happiness positive"
    },
    {
        "value": "social bond particular"
    },
    {
        "value": "drug addiction would"
    },
    {
        "value": "experience poor health"
    },
    {
        "value": "periphery risk gentrification"
    },
    {
        "value": "amenity new"
    },
    {
        "value": "somehow social sustainability"
    },
    {
        "value": "classification cultural amenity"
    },
    {
        "value": "mainly social capital"
    },
    {
        "value": "people know feel"
    },
    {
        "value": "local social bond"
    },
    {
        "value": "culturelles participation activity"
    },
    {
        "value": "increased cultural participation"
    },
    {
        "value": "support project staff"
    },
    {
        "value": "development partnership"
    },
    {
        "value": "decreased activity participation"
    },
    {
        "value": "involvement social activity"
    },
    {
        "value": "facilitate development partnership"
    },
    {
        "value": "build experience working"
    },
    {
        "value": "historic cultural heritage"
    },
    {
        "value": "preservation digital heritage"
    },
    {
        "value": "attractive inward investment"
    },
    {
        "value": "fact place attachment"
    },
    {
        "value": "historic preservation think"
    },
    {
        "value": "improved sense place"
    },
    {
        "value": "developed inward investment"
    },
    {
        "value": "excitement happiness"
    },
    {
        "value": "improved physical wellbeing"
    },
    {
        "value": "creative development industry"
    },
    {
        "value": "program community project"
    },
    {
        "value": "feel like live"
    },
    {
        "value": "involvement activity"
    },
    {
        "value": "project community project"
    },
    {
        "value": "attachment place"
    },
    {
        "value": "heritage publicprivate"
    },
    {
        "value": "preserve historical cultural"
    },
    {
        "value": "social capital many"
    },
    {
        "value": "feeling anxiety concern"
    },
    {
        "value": "creation new industry"
    },
    {
        "value": "intensity feeling anxiety"
    },
    {
        "value": "child development especially"
    },
    {
        "value": "feeling solidarity encounter"
    },
    {
        "value": "new amenity"
    },
    {
        "value": "facilitate development synergy"
    },
    {
        "value": "cluster creative industry"
    },
    {
        "value": "community identity improving"
    },
    {
        "value": "intercultural understanding help"
    },
    {
        "value": "organization community project"
    },
    {
        "value": "leisure shopping facility"
    },
    {
        "value": "experience understanding better"
    },
    {
        "value": "develop community activity"
    },
    {
        "value": "community building organizational"
    },
    {
        "value": "believe community project"
    },
    {
        "value": "social increased social"
    },
    {
        "value": "people feel better"
    },
    {
        "value": "lower cultural capital"
    },
    {
        "value": "confidence feeling"
    },
    {
        "value": "tradition community development"
    },
    {
        "value": "risk brutal gentrification"
    },
    {
        "value": "research child development"
    },
    {
        "value": "job creating"
    },
    {
        "value": "whole community help"
    },
    {
        "value": "conservation heritage"
    },
    {
        "value": "actually make people"
    },
    {
        "value": "sustainability economic efficiency"
    },
    {
        "value": "work community project"
    },
    {
        "value": "contact understanding generation"
    },
    {
        "value": "child child educational"
    },
    {
        "value": "good make feel"
    },
    {
        "value": "gentrification may"
    },
    {
        "value": "help enhance creativity"
    },
    {
        "value": "ecological sustainability"
    },
    {
        "value": "tradition culture"
    },
    {
        "value": "new product industry"
    },
    {
        "value": "future industry development"
    },
    {
        "value": "social sustainability used"
    },
    {
        "value": "happiness joy well"
    },
    {
        "value": "participation activity well"
    },
    {
        "value": "environmental sustainability"
    },
    {
        "value": "local identity enhance"
    },
    {
        "value": "social sustainability many"
    },
    {
        "value": "social capital reducing"
    },
    {
        "value": "enhanced social capital"
    },
    {
        "value": "intercultural contact understanding"
    },
    {
        "value": "inward investment developing"
    },
    {
        "value": "enabling community project"
    },
    {
        "value": "capacity improve community"
    },
    {
        "value": "leisure venue facility"
    },
    {
        "value": "people sense influence"
    },
    {
        "value": "belonging community sense"
    },
    {
        "value": "drug addiction thought"
    },
    {
        "value": "social capital generally"
    },
    {
        "value": "health improved"
    },
    {
        "value": "group drug addiction"
    },
    {
        "value": "mean anxiety reduced"
    },
    {
        "value": "capacity interact"
    },
    {
        "value": "occurring alcohol intake"
    },
    {
        "value": "range cultural amenity"
    },
    {
        "value": "developing local identity"
    },
    {
        "value": "flow tourism"
    },
    {
        "value": "work facilitate development"
    },
    {
        "value": "challenge conventional service"
    },
    {
        "value": "risk therefore encourage"
    },
    {
        "value": "networking cooperation"
    },
    {
        "value": "better understanding public"
    },
    {
        "value": "happiness joy personal"
    },
    {
        "value": "quality people life"
    },
    {
        "value": "project serve community"
    },
    {
        "value": "improving planning design"
    },
    {
        "value": "community development neighborhood"
    },
    {
        "value": "cultural activity amenity"
    },
    {
        "value": "participation support project"
    },
    {
        "value": "participation cultural activity"
    },
    {
        "value": "social capital new"
    },
    {
        "value": "sense improved"
    },
    {
        "value": "participation sort activity"
    },
    {
        "value": "urban planning design"
    },
    {
        "value": "feeling anxiety measured"
    },
    {
        "value": "activity participation insufficient"
    },
    {
        "value": "development child first"
    },
    {
        "value": "cultural amenity regard"
    },
    {
        "value": "development partnership build"
    },
    {
        "value": "community led project"
    },
    {
        "value": "gentrification moreover"
    },
    {
        "value": "sense place"
    },
    {
        "value": "promoting intercultural contact"
    },
    {
        "value": "inward investment good"
    },
    {
        "value": "build local capacity"
    },
    {
        "value": "development formal partnership"
    },
    {
        "value": "sense wellbeing jensen"
    },
    {
        "value": "heritage preserve historic"
    },
    {
        "value": "route place attachment"
    },
    {
        "value": "problem job creation"
    },
    {
        "value": "perception improved"
    },
    {
        "value": "could support community"
    },
    {
        "value": "gentrification sutherland"
    },
    {
        "value": "expectation possible desirable"
    },
    {
        "value": "towards community project"
    },
    {
        "value": "transform image public"
    },
    {
        "value": "tourism attraction"
    },
    {
        "value": "strong feeling anxiety"
    },
    {
        "value": "improved wellbeing however"
    },
    {
        "value": "build support community"
    },
    {
        "value": "place attachment positive"
    },
    {
        "value": "support project furthermore"
    },
    {
        "value": "wellbeing improved social"
    },
    {
        "value": "community identity promote"
    },
    {
        "value": "based leisure facility"
    },
    {
        "value": "erode distinction consumer"
    },
    {
        "value": "individual sense wellbeing"
    },
    {
        "value": "wellbeing improved slightly"
    },
    {
        "value": "live people like"
    },
    {
        "value": "social capital furthermore"
    },
    {
        "value": "creation work"
    },
    {
        "value": "suggested intake alcohol"
    },
    {
        "value": "discrimination wake"
    },
    {
        "value": "community organization support"
    },
    {
        "value": "improved wellbeing especially"
    },
    {
        "value": "building community organizational"
    },
    {
        "value": "project involved community"
    },
    {
        "value": "develop local identity"
    },
    {
        "value": "sustainability energy social"
    },
    {
        "value": "promoting intercultural understanding"
    },
    {
        "value": "discrimination racism sexism"
    },
    {
        "value": "value cultural amenity"
    },
    {
        "value": "sexual behavior standard"
    },
    {
        "value": "town community"
    },
    {
        "value": "capital social redes"
    },
    {
        "value": "project facilitated community"
    },
    {
        "value": "educational community development"
    },
    {
        "value": "support project support"
    },
    {
        "value": "activity social"
    },
    {
        "value": "increased sense belonging"
    },
    {
        "value": "discrimination equality form"
    },
    {
        "value": "enhances social cohesion"
    },
    {
        "value": "social activity reduced"
    },
    {
        "value": "cultural civic amenity"
    },
    {
        "value": "greater knowledge diversity"
    },
    {
        "value": "experience drug addiction"
    },
    {
        "value": "civic sense community"
    },
    {
        "value": "activity produce community"
    },
    {
        "value": "image brand city"
    },
    {
        "value": "civic sense civic"
    },
    {
        "value": "job creation environmental"
    },
    {
        "value": "inward investment contribution"
    },
    {
        "value": "develop contact generation"
    },
    {
        "value": "alcohol intake like"
    },
    {
        "value": "better understanding social"
    },
    {
        "value": "support community initiative"
    },
    {
        "value": "project community involvement"
    },
    {
        "value": "drug addiction led"
    },
    {
        "value": "local talent"
    },
    {
        "value": "enhanced sense wellbeing"
    },
    {
        "value": "resulting gentrification"
    },
    {
        "value": "one better understanding"
    },
    {
        "value": "took training opportunity"
    },
    {
        "value": "research industry development"
    },
    {
        "value": "industry development"
    },
    {
        "value": "wellbeing improved"
    },
    {
        "value": "control life help"
    },
    {
        "value": "reduce feeling anxiety"
    },
    {
        "value": "encourage people accept"
    },
    {
        "value": "insight political social"
    },
    {
        "value": "city branding image"
    },
    {
        "value": "force discrimination racism"
    },
    {
        "value": "development true partnership"
    },
    {
        "value": "professional public voluntary"
    },
    {
        "value": "follow place attachment"
    },
    {
        "value": "activity people community"
    },
    {
        "value": "community community development"
    },
    {
        "value": "heritage whose preservation"
    },
    {
        "value": "discrimination prejudice due"
    },
    {
        "value": "better capacity"
    },
    {
        "value": "community develop network"
    },
    {
        "value": "development cultural industry"
    },
    {
        "value": "facilitate community consultation"
    },
    {
        "value": "improved ability"
    },
    {
        "value": "skill develop new"
    },
    {
        "value": "capital social"
    },
    {
        "value": "approach social sustainability"
    },
    {
        "value": "child development four"
    },
    {
        "value": "reduced depression following"
    },
    {
        "value": "reveal place attachment"
    },
    {
        "value": "industry economic development"
    },
    {
        "value": "enhance social cohesion"
    },
    {
        "value": "cultural preservation"
    },
    {
        "value": "civic sense"
    },
    {
        "value": "providing health education"
    },
    {
        "value": "feeling reduced pain"
    },
    {
        "value": "reduced anxiety restlessness"
    },
    {
        "value": "work skill experience"
    },
    {
        "value": "participation everyday activity"
    },
    {
        "value": "community project whatever"
    },
    {
        "value": "increased alcohol intake"
    },
    {
        "value": "direct discrimination"
    },
    {
        "value": "preservation historic"
    },
    {
        "value": "improved feel place"
    },
    {
        "value": "intake alcohol"
    },
    {
        "value": "participation increased social"
    },
    {
        "value": "support service community"
    },
    {
        "value": "social capital adding"
    },
    {
        "value": "heritage preservation"
    },
    {
        "value": "help validate contribution"
    },
    {
        "value": "social capital national"
    },
    {
        "value": "helping transform image"
    },
    {
        "value": "social sustainability local"
    },
    {
        "value": "better wellbeing"
    },
    {
        "value": "story job creation"
    },
    {
        "value": "context place attachment"
    },
    {
        "value": "better understanding different"
    },
    {
        "value": "pride local tradition"
    },
    {
        "value": "capacity community"
    },
    {
        "value": "depression including feeling"
    },
    {
        "value": "history preservation"
    },
    {
        "value": "build organizational capacity"
    },
    {
        "value": "design overall quality"
    },
    {
        "value": "social activity benefit"
    },
    {
        "value": "heritage preservation issue"
    },
    {
        "value": "development partnership fact"
    },
    {
        "value": "increased participation clarkson"
    },
    {
        "value": "help support community"
    },
    {
        "value": "discrimination instead"
    },
    {
        "value": "decrease social capital"
    },
    {
        "value": "help creativity"
    },
    {
        "value": "job creation tourism"
    },
    {
        "value": "greater sense wellbeing"
    },
    {
        "value": "preserve architectural heritage"
    },
    {
        "value": "sense personal confidence"
    },
    {
        "value": "transform image"
    },
    {
        "value": "development local industry"
    },
    {
        "value": "social capital beyond"
    },
    {
        "value": "preservation heritage try"
    },
    {
        "value": "alcohol intake"
    },
    {
        "value": "sustainability bio ecological"
    },
    {
        "value": "livelihood job creation"
    },
    {
        "value": "improved wellbeing intervention"
    },
    {
        "value": "quality life improving"
    },
    {
        "value": "cultural tourism attraction"
    },
    {
        "value": "group community support"
    },
    {
        "value": "improving social bond"
    },
    {
        "value": "industry development design"
    },
    {
        "value": "social capital second"
    },
    {
        "value": "make people better"
    },
    {
        "value": "social development child"
    },
    {
        "value": "term drug addiction"
    },
    {
        "value": "enhancement local identity"
    },
    {
        "value": "project initiated community"
    },
    {
        "value": "improve wellbeing"
    },
    {
        "value": "new skill expertise"
    },
    {
        "value": "health education provide"
    },
    {
        "value": "racism discrimination acceptance"
    },
    {
        "value": "taken training opportunity"
    },
    {
        "value": "cultural amenity reveals"
    },
    {
        "value": "close cultural amenity"
    },
    {
        "value": "influence young people"
    },
    {
        "value": "building social bond"
    },
    {
        "value": "build experience"
    },
    {
        "value": "intake alcohol related"
    },
    {
        "value": "better understanding community"
    },
    {
        "value": "experienced reduced anxiety"
    },
    {
        "value": "talent local"
    },
    {
        "value": "project help support"
    },
    {
        "value": "community project enabled"
    },
    {
        "value": "like make feel"
    },
    {
        "value": "maintain sense wellbeing"
    },
    {
        "value": "activity public participation"
    },
    {
        "value": "identity enhanced opportunity"
    },
    {
        "value": "belonging sense community"
    },
    {
        "value": "propinquity cultural amenity"
    },
    {
        "value": "pleasure happiness joy"
    },
    {
        "value": "facilitate local consultation"
    },
    {
        "value": "preserving historical"
    },
    {
        "value": "therefore social capital"
    },
    {
        "value": "job creation new"
    },
    {
        "value": "danger partial gentrification"
    },
    {
        "value": "social capital well"
    },
    {
        "value": "job creation data"
    },
    {
        "value": "social activity also"
    },
    {
        "value": "namely social capital"
    },
    {
        "value": "sexual attitude sexual"
    },
    {
        "value": "culture facility leisure"
    },
    {
        "value": "perception awareness community"
    },
    {
        "value": "support creative industry"
    },
    {
        "value": "attachment sense place"
    },
    {
        "value": "relaxed atmosphere might"
    },
    {
        "value": "quality people"
    },
    {
        "value": "improving life quality"
    },
    {
        "value": "inward investment tourism"
    },
    {
        "value": "community project funded"
    },
    {
        "value": "organizational capacity"
    },
    {
        "value": "improved wellbeing difficulty"
    },
    {
        "value": "risk gentrification economic"
    },
    {
        "value": "better understanding elderly"
    },
    {
        "value": "community project based"
    },
    {
        "value": "development one child"
    },
    {
        "value": "health quality life"
    },
    {
        "value": "make feel like"
    },
    {
        "value": "creative sector support"
    },
    {
        "value": "support project would"
    },
    {
        "value": "sustainable ecological"
    },
    {
        "value": "capital government social"
    },
    {
        "value": "build community capacity"
    },
    {
        "value": "reduced feeling fatigue"
    },
    {
        "value": "community project may"
    },
    {
        "value": "sense place attachment"
    },
    {
        "value": "people quality life"
    },
    {
        "value": "industry regional development"
    },
    {
        "value": "alcohol intake negative"
    },
    {
        "value": "city image"
    },
    {
        "value": "job creation sufficient"
    },
    {
        "value": "contribute people employability"
    },
    {
        "value": "local identity local"
    },
    {
        "value": "community place attachment"
    },
    {
        "value": "explore value meaning"
    },
    {
        "value": "social activity even"
    },
    {
        "value": "cultural amenity make"
    },
    {
        "value": "mood reduced anxiety"
    },
    {
        "value": "social group bond"
    },
    {
        "value": "preserve cultural heritage"
    },
    {
        "value": "greater civic"
    },
    {
        "value": "job wealth creation"
    },
    {
        "value": "forum intercultural"
    },
    {
        "value": "place sense"
    },
    {
        "value": "led anxiety feeling"
    },
    {
        "value": "social involvement"
    },
    {
        "value": "increasing pride culture"
    },
    {
        "value": "creation project community"
    },
    {
        "value": "funding support project"
    },
    {
        "value": "anxiety depression increased"
    },
    {
        "value": "community project time"
    },
    {
        "value": "depression feel"
    },
    {
        "value": "sustainability ecological aspect"
    },
    {
        "value": "project community partner"
    },
    {
        "value": "particular reduced depression"
    },
    {
        "value": "wellbeing intervention improved"
    },
    {
        "value": "culture tradition developed"
    },
    {
        "value": "sense wellbeing satisfaction"
    },
    {
        "value": "heritage conservation"
    },
    {
        "value": "addicted drug"
    },
    {
        "value": "culture tradition support"
    },
    {
        "value": "culture industry development"
    },
    {
        "value": "community project working"
    },
    {
        "value": "use skill work"
    },
    {
        "value": "cultural heritage historic"
    },
    {
        "value": "looking job creation"
    },
    {
        "value": "however gentrification"
    },
    {
        "value": "people attachment place"
    },
    {
        "value": "preserving historical architecture"
    },
    {
        "value": "abuse discrimination although"
    },
    {
        "value": "sustainability global social"
    },
    {
        "value": "tradition planning culture"
    },
    {
        "value": "job creation"
    },
    {
        "value": "sustainability also economic"
    },
    {
        "value": "improved ability make"
    },
    {
        "value": "love happiness sadness"
    },
    {
        "value": "like make people"
    },
    {
        "value": "social bond one"
    },
    {
        "value": "development child still"
    },
    {
        "value": "community development community"
    },
    {
        "value": "understanding expression diversity"
    },
    {
        "value": "involved social activity"
    },
    {
        "value": "extend control life"
    },
    {
        "value": "community organizational capacity"
    },
    {
        "value": "industry new"
    },
    {
        "value": "affect ability communicate"
    },
    {
        "value": "sustainability economic"
    },
    {
        "value": "build capacity local"
    },
    {
        "value": "influence seen others"
    },
    {
        "value": "creation social sustainability"
    },
    {
        "value": "think live others"
    },
    {
        "value": "support community project"
    },
    {
        "value": "capital community higher"
    },
    {
        "value": "improved ability cope"
    },
    {
        "value": "sustainability meant social"
    },
    {
        "value": "local cultural tradition"
    },
    {
        "value": "issue drug addiction"
    },
    {
        "value": "preserve historical"
    },
    {
        "value": "social capital particularly"
    },
    {
        "value": "community sense belonging"
    },
    {
        "value": "place attachment rather"
    },
    {
        "value": "child social development"
    },
    {
        "value": "museum cultural amenity"
    },
    {
        "value": "library inward investment"
    },
    {
        "value": "gentrification hurriedness"
    },
    {
        "value": "community identity"
    },
    {
        "value": "sport leisure facility"
    },
    {
        "value": "build new skill"
    },
    {
        "value": "job creation best"
    },
    {
        "value": "feeling unease anxiety"
    },
    {
        "value": "reduced depression anxiety"
    },
    {
        "value": "project support several"
    },
    {
        "value": "ecological sustainability need"
    },
    {
        "value": "extended activity"
    },
    {
        "value": "influence people different"
    },
    {
        "value": "pay cultural amenity"
    },
    {
        "value": "reduced anxiety depression"
    },
    {
        "value": "creation value job"
    },
    {
        "value": "enhanced wellbeing"
    },
    {
        "value": "strong social capital"
    },
    {
        "value": "assumption discrimination"
    },
    {
        "value": "joy happiness also"
    },
    {
        "value": "discrimination right"
    },
    {
        "value": "public consultation participation"
    },
    {
        "value": "depression anxiety increased"
    },
    {
        "value": "opinion regard"
    },
    {
        "value": "poor quality"
    },
    {
        "value": "immediate community project"
    },
    {
        "value": "thought feeling anxiety"
    },
    {
        "value": "community awareness right"
    },
    {
        "value": "development strategic partnership"
    },
    {
        "value": "feeling people involvement"
    },
    {
        "value": "resident environmental improvement"
    },
    {
        "value": "behavior sexual pressure"
    },
    {
        "value": "people actually make"
    },
    {
        "value": "creative industry support"
    },
    {
        "value": "sense community belonging"
    },
    {
        "value": "project community level"
    },
    {
        "value": "help develop skill"
    },
    {
        "value": "feeling anxiety stress"
    },
    {
        "value": "development support community"
    },
    {
        "value": "place attachment"
    },
    {
        "value": "society job creation"
    },
    {
        "value": "alcohol intake human"
    },
    {
        "value": "community identity help"
    },
    {
        "value": "tradition culture belief"
    },
    {
        "value": "improved sense"
    },
    {
        "value": "identity experience enhanced"
    },
    {
        "value": "cultural heritage pride"
    },
    {
        "value": "reduced anxiety anger"
    },
    {
        "value": "support development child"
    },
    {
        "value": "local heritage culture"
    },
    {
        "value": "promote intercultural contact"
    },
    {
        "value": "depression boosting feeling"
    },
    {
        "value": "preservation architectural heritage"
    },
    {
        "value": "gentrification gentrification multifaceted"
    },
    {
        "value": "improve quality life"
    },
    {
        "value": "institution joy happiness"
    },
    {
        "value": "probably make feel"
    },
    {
        "value": "early child development"
    },
    {
        "value": "targeted community project"
    },
    {
        "value": "improved wellbeing creativity"
    },
    {
        "value": "community tradition new"
    },
    {
        "value": "build skill needed"
    },
    {
        "value": "feeling stress anxiety"
    },
    {
        "value": "intercultural contact co"
    },
    {
        "value": "better understanding interaction"
    },
    {
        "value": "result gentrification"
    },
    {
        "value": "social participation reduced"
    },
    {
        "value": "social capital longer"
    },
    {
        "value": "social bond family"
    },
    {
        "value": "accept risk positively"
    },
    {
        "value": "social ecological sustainability"
    },
    {
        "value": "social capital suggesting"
    },
    {
        "value": "wellbeing improved participation"
    },
    {
        "value": "participation group activity"
    },
    {
        "value": "amenity cultural district"
    },
    {
        "value": "isolation helping people"
    },
    {
        "value": "wealth job creation"
    },
    {
        "value": "collec community project"
    },
    {
        "value": "feeling happiness joy"
    },
    {
        "value": "improving life people"
    },
    {
        "value": "change discrimination"
    },
    {
        "value": "project meeting community"
    },
    {
        "value": "social capital thus"
    },
    {
        "value": "organizational capacity development"
    },
    {
        "value": "professional voluntary sector"
    },
    {
        "value": "validate contribution whole"
    },
    {
        "value": "higher one social"
    },
    {
        "value": "social sustainability also"
    },
    {
        "value": "activity participation ongoing"
    },
    {
        "value": "pride excitement neighborhood"
    },
    {
        "value": "participation community project"
    },
    {
        "value": "development partnership community"
    },
    {
        "value": "social cohesion improved"
    },
    {
        "value": "pride particular culture"
    },
    {
        "value": "help build skill"
    },
    {
        "value": "improved wellbeing"
    },
    {
        "value": "new skill contribute"
    },
    {
        "value": "especially project community"
    },
    {
        "value": "sustainability environmental"
    },
    {
        "value": "help people develop"
    },
    {
        "value": "make feel good"
    },
    {
        "value": "preservation recorded heritage"
    },
    {
        "value": "community capacity"
    },
    {
        "value": "anxiety feeling powerlessness"
    },
    {
        "value": "around social capital"
    },
    {
        "value": "inward investment least"
    },
    {
        "value": "development young child"
    },
    {
        "value": "improve quality people"
    },
    {
        "value": "reducing anxiety depression"
    },
    {
        "value": "intercultural contact"
    },
    {
        "value": "good quality life"
    },
    {
        "value": "business new industry"
    },
    {
        "value": "gentrification gentrification medium"
    },
    {
        "value": "make people want"
    },
    {
        "value": "intercultural understanding friendship"
    },
    {
        "value": "cultural amenity"
    },
    {
        "value": "promote development industry"
    },
    {
        "value": "social bond also"
    },
    {
        "value": "intercultural understanding nevertheless"
    },
    {
        "value": "intercultural understanding"
    },
    {
        "value": "social capital although"
    },
    {
        "value": "appropriate behavior"
    },
    {
        "value": "strengthening social bond"
    },
    {
        "value": "increasing social participation"
    },
    {
        "value": "industry development concept"
    },
    {
        "value": "capital social capital"
    },
    {
        "value": "historical understanding heritage"
    },
    {
        "value": "better understanding human"
    },
    {
        "value": "project community"
    },
    {
        "value": "social increased"
    },
    {
        "value": "development partnership working"
    },
    {
        "value": "others influence"
    },
    {
        "value": "ability make communicate"
    },
    {
        "value": "activity participation high"
    },
    {
        "value": "boom risk gentrification"
    },
    {
        "value": "develop community people"
    },
    {
        "value": "social capital boosting"
    },
    {
        "value": "social capital level"
    },
    {
        "value": "environment tradition culture"
    },
    {
        "value": "capital higher"
    },
    {
        "value": "danger gentrification"
    },
    {
        "value": "kind support community"
    },
    {
        "value": "concept gentrification gentrification"
    },
    {
        "value": "feeling sense wellbeing"
    },
    {
        "value": "intercultural contact collaboration"
    },
    {
        "value": "amenity supporting cultural"
    },
    {
        "value": "sense place overall"
    },
    {
        "value": "importance better understanding"
    },
    {
        "value": "activity increased"
    },
    {
        "value": "involve regeneration"
    },
    {
        "value": "development feeling solidarity"
    },
    {
        "value": "feeling happiness"
    },
    {
        "value": "development industry related"
    },
    {
        "value": "design industry new"
    },
    {
        "value": "activity community participation"
    },
    {
        "value": "tourism attraction however"
    },
    {
        "value": "amenity diverse cultural"
    },
    {
        "value": "sex behavior"
    },
    {
        "value": "investment job creation"
    },
    {
        "value": "perception reduced anxiety"
    },
    {
        "value": "capital adding social"
    },
    {
        "value": "preservation cultural heritage"
    },
    {
        "value": "anxiety experiencing feeling"
    },
    {
        "value": "make people feel"
    },
    {
        "value": "largest drug addiction"
    },
    {
        "value": "feeling anxiety discomfort"
    },
    {
        "value": "development pride heritage"
    },
    {
        "value": "heritage preservation old"
    },
    {
        "value": "cultural amenity amenity"
    },
    {
        "value": "industry new way"
    },
    {
        "value": "build capacity community"
    },
    {
        "value": "possible gentrification"
    },
    {
        "value": "cultural amenity minor"
    },
    {
        "value": "urban design planning"
    },
    {
        "value": "social sustainability case"
    },
    {
        "value": "amenity unique"
    },
    {
        "value": "support community event"
    },
    {
        "value": "higher cultural capital"
    },
    {
        "value": "attachment increased"
    },
    {
        "value": "inflow tourist"
    },
    {
        "value": "preserving heritage"
    },
    {
        "value": "support future project"
    },
    {
        "value": "economic sustainability"
    },
    {
        "value": "provide reason people"
    },
    {
        "value": "robust social sustainability"
    },
    {
        "value": "broader industry development"
    },
    {
        "value": "child biopsychosocial development"
    },
    {
        "value": "historical built heritage"
    },
    {
        "value": "identity enhanced together"
    },
    {
        "value": "historic cultural preservation"
    },
    {
        "value": "capacity develop community"
    },
    {
        "value": "influence way people"
    },
    {
        "value": "resulting improved wellbeing"
    },
    {
        "value": "real sense wellbeing"
    },
    {
        "value": "rehabilitation integration offender"
    },
    {
        "value": "brand image city"
    },
    {
        "value": "reduced drug"
    },
    {
        "value": "higher social capital"
    },
    {
        "value": "attraction tourism"
    },
    {
        "value": "increased feeling"
    },
    {
        "value": "historical amenity cultural"
    },
    {
        "value": "creation new job"
    },
    {
        "value": "people develop"
    },
    {
        "value": "employability help people"
    },
    {
        "value": "local identity expanding"
    },
    {
        "value": "place attachment inclusion"
    },
    {
        "value": "pride culture"
    },
    {
        "value": "people feel way"
    },
    {
        "value": "people go feel"
    },
    {
        "value": "enhance contribution community"
    },
    {
        "value": "giving sense wellbeing"
    },
    {
        "value": "quality life better"
    },
    {
        "value": "result social activity"
    },
    {
        "value": "community project still"
    },
    {
        "value": "drug addiction cost"
    },
    {
        "value": "increased intake alcohol"
    },
    {
        "value": "drug addiction impact"
    },
    {
        "value": "increase civic"
    },
    {
        "value": "related sexual behavior"
    },
    {
        "value": "project within community"
    },
    {
        "value": "place attachment sense"
    },
    {
        "value": "development local talent"
    },
    {
        "value": "help offender victim"
    },
    {
        "value": "forum explore personal"
    },
    {
        "value": "influence seen"
    },
    {
        "value": "also influence people"
    },
    {
        "value": "case discrimination"
    },
    {
        "value": "tourism flow"
    },
    {
        "value": "art cultural amenity"
    },
    {
        "value": "development facilitate"
    },
    {
        "value": "social activity decrease"
    },
    {
        "value": "sense belonging feel"
    },
    {
        "value": "job creation innovation"
    },
    {
        "value": "desire ability communicate"
    },
    {
        "value": "cooperation community"
    },
    {
        "value": "social activity increased"
    },
    {
        "value": "new place attachment"
    },
    {
        "value": "better capacity create"
    },
    {
        "value": "development local culture"
    },
    {
        "value": "reliance project management"
    },
    {
        "value": "reduced depression depressive"
    },
    {
        "value": "one gentrification"
    },
    {
        "value": "find community project"
    },
    {
        "value": "community network sociability"
    },
    {
        "value": "social capital within"
    },
    {
        "value": "much social capital"
    },
    {
        "value": "community project three"
    },
    {
        "value": "community cooperation"
    },
    {
        "value": "enhance identity"
    },
    {
        "value": "increased activity"
    },
    {
        "value": "community large project"
    },
    {
        "value": "wellbeing following improved"
    },
    {
        "value": "social sustainability design"
    },
    {
        "value": "service support community"
    },
    {
        "value": "social capital good"
    },
    {
        "value": "social bond"
    },
    {
        "value": "industry development public"
    },
    {
        "value": "government support community"
    },
    {
        "value": "social capital larger"
    },
    {
        "value": "community project"
    },
    {
        "value": "involvement cultural activity"
    },
    {
        "value": "better understanding cultural"
    },
    {
        "value": "social activity overall"
    },
    {
        "value": "quality life improved"
    },
    {
        "value": "culture local development"
    },
    {
        "value": "ability communicate among"
    },
    {
        "value": "participate social activity"
    },
    {
        "value": "industry urban development"
    },
    {
        "value": "quality poor"
    },
    {
        "value": "identity well community"
    },
    {
        "value": "community base project"
    },
    {
        "value": "cultural amenity transport"
    },
    {
        "value": "partnership community support"
    },
    {
        "value": "reduced anxiety better"
    },
    {
        "value": "improved perception"
    },
    {
        "value": "community social bond"
    },
    {
        "value": "place attachment civic"
    },
    {
        "value": "urban design significantly"
    },
    {
        "value": "architectural quality urban"
    },
    {
        "value": "lower anxiety depression"
    },
    {
        "value": "center periphery"
    },
    {
        "value": "made feel better"
    },
    {
        "value": "activity social participation"
    },
    {
        "value": "belonging place attachment"
    },
    {
        "value": "amenity cultural"
    },
    {
        "value": "development child youth"
    },
    {
        "value": "increased engagement activity"
    },
    {
        "value": "community partner project"
    },
    {
        "value": "growth economic sustainability"
    },
    {
        "value": "educational development personal"
    },
    {
        "value": "facilitate collaboration partnership"
    },
    {
        "value": "feel good people"
    },
    {
        "value": "cultural amenity major"
    },
    {
        "value": "joy happiness sense"
    },
    {
        "value": "sexual behavior choice"
    },
    {
        "value": "community involved project"
    },
    {
        "value": "feel good make"
    },
    {
        "value": "valorizing preserving historical"
    },
    {
        "value": "development industry government"
    },
    {
        "value": "community project initially"
    },
    {
        "value": "activity individual participation"
    },
    {
        "value": "awareness community"
    },
    {
        "value": "consultation participation help"
    },
    {
        "value": "high self esteem"
    },
    {
        "value": "depression reduced anxiety"
    },
    {
        "value": "indicate place attachment"
    },
    {
        "value": "layered attachment place"
    },
    {
        "value": "level job creation"
    },
    {
        "value": "community project much"
    },
    {
        "value": "community group project"
    },
    {
        "value": "local identity well"
    },
    {
        "value": "child life educational"
    },
    {
        "value": "low self esteem"
    },
    {
        "value": "self esteem increased"
    },
    {
        "value": "increased competitiveness"
    },
    {
        "value": "gentrification possible"
    },
    {
        "value": "sexual behavior boy"
    },
    {
        "value": "area inward investment"
    },
    {
        "value": "improved social capital"
    },
    {
        "value": "strengthening local identity"
    },
    {
        "value": "development new partnership"
    },
    {
        "value": "heritage cultural historical"
    },
    {
        "value": "social activity significant"
    },
    {
        "value": "extend involvement social"
    },
    {
        "value": "community project group"
    },
    {
        "value": "new industry development"
    },
    {
        "value": "sustainability ecological sustainability"
    },
    {
        "value": "support project"
    },
    {
        "value": "level social capital"
    },
    {
        "value": "activity substantial social"
    },
    {
        "value": "economic sustainability perhaps"
    },
    {
        "value": "caused drug addiction"
    },
    {
        "value": "attachment increased place"
    },
    {
        "value": "enhanced social cohesion"
    },
    {
        "value": "community support build"
    },
    {
        "value": "urban heritage preservation"
    },
    {
        "value": "quality life improve"
    },
    {
        "value": "community project including"
    },
    {
        "value": "well local identity"
    },
    {
        "value": "increase social capital"
    },
    {
        "value": "reshaping city image"
    },
    {
        "value": "amenity primarily cultural"
    },
    {
        "value": "scale cultural amenity"
    },
    {
        "value": "activity strong participation"
    },
    {
        "value": "new skill work"
    },
    {
        "value": "sex behavior sexual"
    },
    {
        "value": "place secure attachment"
    },
    {
        "value": "helping people develop"
    },
    {
        "value": "better understanding culture"
    },
    {
        "value": "social sustainability building"
    },
    {
        "value": "global partnership development"
    },
    {
        "value": "cultural industry development"
    },
    {
        "value": "anxiety lessened"
    },
    {
        "value": "participation activity group"
    },
    {
        "value": "wellbeing sense"
    },
    {
        "value": "relevant heritage preservation"
    },
    {
        "value": "feel better"
    },
    {
        "value": "place attachment whereas"
    },
    {
        "value": "image city positioning"
    },
    {
        "value": "discrimination could"
    },
    {
        "value": "source job creation"
    },
    {
        "value": "happiness joy positive"
    },
    {
        "value": "promoting sense wellbeing"
    },
    {
        "value": "joy contentment"
    },
    {
        "value": "development child encourage"
    },
    {
        "value": "involvement sense belonging"
    },
    {
        "value": "relaxed atmosphere"
    },
    {
        "value": "enhanced sense identity"
    },
    {
        "value": "non discrimination"
    },
    {
        "value": "strengthening sense place"
    },
    {
        "value": "activity bring people"
    },
    {
        "value": "alcohol intake behavior"
    },
    {
        "value": "youth understanding meaning"
    },
    {
        "value": "quality life health"
    },
    {
        "value": "people feel good"
    },
    {
        "value": "characterized happiness joy"
    },
    {
        "value": "participation urban"
    },
    {
        "value": "place attachment perceived"
    },
    {
        "value": "people feel really"
    },
    {
        "value": "development child see"
    },
    {
        "value": "closer social bond"
    },
    {
        "value": "partnership development leadership"
    },
    {
        "value": "image city branding"
    },
    {
        "value": "value meaning dream"
    },
    {
        "value": "meaning understanding social"
    },
    {
        "value": "social sustainability whole"
    },
    {
        "value": "engage health"
    },
    {
        "value": "leisure activity facility"
    },
    {
        "value": "approach drug addiction"
    },
    {
        "value": "cultural heritage conservation"
    },
    {
        "value": "training education opportunity"
    },
    {
        "value": "people want live"
    },
    {
        "value": "reason people develop"
    },
    {
        "value": "reinvention city image"
    },
    {
        "value": "boosting local identity"
    },
    {
        "value": "historic preservation art"
    },
    {
        "value": "project community based"
    },
    {
        "value": "personal development industry"
    },
    {
        "value": "ability communicate experience"
    },
    {
        "value": "increased confidence feeling"
    },
    {
        "value": "development participation activity"
    },
    {
        "value": "development educational"
    },
    {
        "value": "contact generation"
    },
    {
        "value": "project support also"
    },
    {
        "value": "community project could"
    },
    {
        "value": "people going feel"
    },
    {
        "value": "joy contentment excitement"
    },
    {
        "value": "racism discrimination"
    },
    {
        "value": "community service project"
    },
    {
        "value": "attachment joint place"
    },
    {
        "value": "ascribed cultural amenity"
    },
    {
        "value": "life quality local"
    },
    {
        "value": "society place attachment"
    },
    {
        "value": "social bond civic"
    },
    {
        "value": "well place attachment"
    },
    {
        "value": "improved social cohesion"
    },
    {
        "value": "place attachment relation"
    },
    {
        "value": "social economic sustainability"
    },
    {
        "value": "part social activity"
    },
    {
        "value": "job creation fostering"
    },
    {
        "value": "term industry development"
    },
    {
        "value": "based social sustainability"
    },
    {
        "value": "learning improved ability"
    },
    {
        "value": "historical heritage building"
    },
    {
        "value": "development child psychosocial"
    },
    {
        "value": "experience work need"
    },
    {
        "value": "social exclusion discrimination"
    },
    {
        "value": "poorer quality life"
    },
    {
        "value": "way offender address"
    },
    {
        "value": "enhancing sense place"
    },
    {
        "value": "preservation historical asset"
    },
    {
        "value": "raise expectation possible"
    },
    {
        "value": "increased participation"
    },
    {
        "value": "tourist flow attraction"
    },
    {
        "value": "sexual behavior prevalent"
    },
    {
        "value": "feel like make"
    },
    {
        "value": "social value sustainability"
    },
    {
        "value": "sustainability important economic"
    },
    {
        "value": "risk producing gentrification"
    },
    {
        "value": "social capital among"
    },
    {
        "value": "increase social participation"
    },
    {
        "value": "support build community"
    },
    {
        "value": "gentrification resulting"
    },
    {
        "value": "community education project"
    },
    {
        "value": "accessibility leisure facility"
    },
    {
        "value": "city community support"
    },
    {
        "value": "reduced anxiety travers"
    },
    {
        "value": "increased civic"
    },
    {
        "value": "improve ability"
    },
    {
        "value": "cultural development industry"
    },
    {
        "value": "design social sustainability"
    },
    {
        "value": "wellbeing improved physical"
    },
    {
        "value": "tradition group culture"
    },
    {
        "value": "innovation economic sustainability"
    },
    {
        "value": "address young offender"
    },
    {
        "value": "neighborhood higher"
    },
    {
        "value": "new job creation"
    },
    {
        "value": "greater self esteem"
    },
    {
        "value": "addiction among drug"
    },
    {
        "value": "offender address"
    },
    {
        "value": "heritage preservation figure"
    },
    {
        "value": "community project work"
    },
    {
        "value": "feeling despair depression"
    },
    {
        "value": "cooperation networking"
    },
    {
        "value": "wellbeing enhanced"
    },
    {
        "value": "sustainability economic development"
    },
    {
        "value": "building community project"
    },
    {
        "value": "confidence personal"
    },
    {
        "value": "two social capital"
    },
    {
        "value": "without discrimination"
    },
    {
        "value": "prosperity inward investment"
    },
    {
        "value": "poor health enhancing"
    },
    {
        "value": "social capital local"
    },
    {
        "value": "bias discrimination"
    },
    {
        "value": "building organizational capacity"
    },
    {
        "value": "recovery drug addiction"
    },
    {
        "value": "imply positive discrimination"
    },
    {
        "value": "tourism attraction capacity"
    },
    {
        "value": "greater sense belonging"
    },
    {
        "value": "social sustainability"
    },
    {
        "value": "feel like people"
    },
    {
        "value": "anxiety one feel"
    },
    {
        "value": "enhance sense place"
    },
    {
        "value": "way make feel"
    },
    {
        "value": "heritage cultural heritage"
    },
    {
        "value": "inward investment local"
    },
    {
        "value": "noted improved wellbeing"
    },
    {
        "value": "work creation"
    },
    {
        "value": "risk gentrification"
    },
    {
        "value": "job creation surprising"
    },
    {
        "value": "youth community project"
    },
    {
        "value": "fostering better understanding"
    },
    {
        "value": "develop new skill"
    },
    {
        "value": "industry job creation"
    },
    {
        "value": "way people feel"
    },
    {
        "value": "wellbeing sense place"
    },
    {
        "value": "little ability communicate"
    },
    {
        "value": "increased place attachment"
    },
    {
        "value": "place attachment recent"
    },
    {
        "value": "sense community decreasing"
    },
    {
        "value": "enhanced quality life"
    },
    {
        "value": "overall urban design"
    },
    {
        "value": "gaining insight political"
    },
    {
        "value": "area cultural amenity"
    },
    {
        "value": "social involvement active"
    },
    {
        "value": "anxiety felt"
    },
    {
        "value": "people made feel"
    },
    {
        "value": "reduced level anxiety"
    },
    {
        "value": "reported sexual behavior"
    },
    {
        "value": "ability communicate one"
    },
    {
        "value": "elitist cultural amenity"
    },
    {
        "value": "skill new experience"
    },
    {
        "value": "people live make"
    },
    {
        "value": "improving quality people"
    },
    {
        "value": "local community project"
    },
    {
        "value": "people poor health"
    },
    {
        "value": "participation activity little"
    },
    {
        "value": "development industry based"
    },
    {
        "value": "kind bias discrimination"
    },
    {
        "value": "amount alcohol intake"
    },
    {
        "value": "facilitate development new"
    },
    {
        "value": "place attachment potential"
    },
    {
        "value": "wellbeing improved course"
    },
    {
        "value": "local tradition culture"
    },
    {
        "value": "increased alcohol"
    },
    {
        "value": "job creation total"
    },
    {
        "value": "facility leisure"
    },
    {
        "value": "inappropriate type behavior"
    },
    {
        "value": "therefore gentrification"
    },
    {
        "value": "manufacturing industry new"
    },
    {
        "value": "social activity participation"
    },
    {
        "value": "build skill"
    },
    {
        "value": "people extend control"
    },
    {
        "value": "system support community"
    },
    {
        "value": "wellbeing strong sense"
    },
    {
        "value": "inward investment traditional"
    },
    {
        "value": "sexism discrimination"
    },
    {
        "value": "particular culture tradition"
    },
    {
        "value": "local people regeneration"
    },
    {
        "value": "activity greater social"
    },
    {
        "value": "reference sustainability ecological"
    },
    {
        "value": "social capital therefore"
    },
    {
        "value": "offender address problem"
    },
    {
        "value": "depression felt"
    },
    {
        "value": "cultural development partnership"
    },
    {
        "value": "see people make"
    },
    {
        "value": "however preservation cultural"
    },
    {
        "value": "social capital would"
    },
    {
        "value": "company project support"
    },
    {
        "value": "take develop career"
    },
    {
        "value": "communal meaning required"
    },
    {
        "value": "poor health"
    },
    {
        "value": "making community project"
    },
    {
        "value": "community project even"
    },
    {
        "value": "activity people develop"
    },
    {
        "value": "social capital third"
    },
    {
        "value": "drug addiction issue"
    },
    {
        "value": "discrimination simply"
    },
    {
        "value": "quality architectural urban"
    },
    {
        "value": "gentrification perceived"
    },
    {
        "value": "preservation cultural"
    },
    {
        "value": "especially social sustainability"
    },
    {
        "value": "industry new business"
    },
    {
        "value": "build organizational"
    },
    {
        "value": "develop skill"
    },
    {
        "value": "social capital substantial"
    },
    {
        "value": "place attachment among"
    },
    {
        "value": "curriculum educational development"
    },
    {
        "value": "participation activity freud"
    },
    {
        "value": "discrimination especially"
    },
    {
        "value": "social capital related"
    },
    {
        "value": "drug addiction jess"
    },
    {
        "value": "depression wellbeing improved"
    },
    {
        "value": "social capital overall"
    },
    {
        "value": "led community project"
    },
    {
        "value": "unprotected sexual behavior"
    },
    {
        "value": "enhancing social cohesion"
    },
    {
        "value": "project local community"
    },
    {
        "value": "training opportunity care"
    }
]

IMPACT_KEYWORDS_M2M = [
    {
        "impact": IMPACTS[0],
        "keyword": IMPACT_KEYWORDS[2036]
    },
    {
        "impact": IMPACTS[0],
        "keyword": IMPACT_KEYWORDS[1585]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[689]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1160]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1774]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1810]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[128]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1551]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[2228]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1397]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[976]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[2180]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1998]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[2161]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[240]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1871]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[227]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[706]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1969]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1087]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[95]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[2087]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[189]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1684]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1078]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[1947]
    },
    {
        "impact": IMPACTS[1],
        "keyword": IMPACT_KEYWORDS[982]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1265]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1692]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2067]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1873]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[454]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1215]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2151]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1618]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1584]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1480]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1985]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[148]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1958]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2062]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1033]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[397]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2069]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1959]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[825]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[254]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[904]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2219]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1254]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[686]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2150]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[714]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1999]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1936]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[164]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2174]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2010]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[462]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1175]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2030]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[2065]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[11]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[861]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1889]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1651]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[487]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1375]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1555]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1363]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[354]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1226]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1576]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[905]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[953]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[453]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[986]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1929]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1858]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[703]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1454]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[1439]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[281]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[131]
    },
    {
        "impact": IMPACTS[2],
        "keyword": IMPACT_KEYWORDS[963]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[583]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1758]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[105]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1257]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1970]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1654]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[2188]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[2138]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1358]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1559]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[318]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[790]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1253]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[465]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[424]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[977]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[84]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[134]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[261]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[2123]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[72]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1316]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[945]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[1416]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[160]
    },
    {
        "impact": IMPACTS[3],
        "keyword": IMPACT_KEYWORDS[927]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1880]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1851]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1832]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1331]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1371]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[939]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1808]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1069]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[2130]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[452]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1094]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[766]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[763]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[903]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[503]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[280]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[852]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[2086]
    },
    {
        "impact": IMPACTS[4],
        "keyword": IMPACT_KEYWORDS[1509]
    },
    {
        "impact": IMPACTS[5],
        "keyword": IMPACT_KEYWORDS[2039]
    },
    {
        "impact": IMPACTS[5],
        "keyword": IMPACT_KEYWORDS[1023]
    },
    {
        "impact": IMPACTS[5],
        "keyword": IMPACT_KEYWORDS[1459]
    },
    {
        "impact": IMPACTS[5],
        "keyword": IMPACT_KEYWORDS[1521]
    },
    {
        "impact": IMPACTS[5],
        "keyword": IMPACT_KEYWORDS[675]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1656]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[82]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[107]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[121]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1954]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1277]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[767]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[997]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1378]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1553]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1695]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1922]
    },
    {
        "impact": IMPACTS[6],
        "keyword": IMPACT_KEYWORDS[1680]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[941]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[936]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[1444]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[750]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[1327]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[198]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[770]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[806]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[514]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[1122]
    },
    {
        "impact": IMPACTS[7],
        "keyword": IMPACT_KEYWORDS[1890]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[102]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[146]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[811]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1336]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1038]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[959]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1173]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1186]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1717]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[110]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[573]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[724]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1564]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1780]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[2203]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1419]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[855]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1530]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[2037]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[2025]
    },
    {
        "impact": IMPACTS[8],
        "keyword": IMPACT_KEYWORDS[1140]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[931]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1076]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1052]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1281]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1426]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1481]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[512]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1800]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[225]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[2144]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[983]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[329]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1914]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1183]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[495]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[837]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[2001]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[612]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1530]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[644]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[723]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1631]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[306]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1409]
    },
    {
        "impact": IMPACTS[9],
        "keyword": IMPACT_KEYWORDS[1196]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1561]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[2216]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1483]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1755]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1638]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1359]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1634]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[445]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1736]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[748]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1390]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1573]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1318]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[2127]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1283]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1843]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[510]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[924]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[122]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[83]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[22]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1486]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[155]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[1823]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[100]
    },
    {
        "impact": IMPACTS[10],
        "keyword": IMPACT_KEYWORDS[214]
    },
    {
        "impact": IMPACTS[11],
        "keyword": IMPACT_KEYWORDS[469]
    },
    {
        "impact": IMPACTS[11],
        "keyword": IMPACT_KEYWORDS[1333]
    },
    {
        "impact": IMPACTS[11],
        "keyword": IMPACT_KEYWORDS[818]
    },
    {
        "impact": IMPACTS[12],
        "keyword": IMPACT_KEYWORDS[13]
    },
    {
        "impact": IMPACTS[12],
        "keyword": IMPACT_KEYWORDS[1103]
    },
    {
        "impact": IMPACTS[12],
        "keyword": IMPACT_KEYWORDS[470]
    },
    {
        "impact": IMPACTS[12],
        "keyword": IMPACT_KEYWORDS[1582]
    },
    {
        "impact": IMPACTS[12],
        "keyword": IMPACT_KEYWORDS[1856]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[1204]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[1398]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[1289]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[1713]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[1341]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[194]
    },
    {
        "impact": IMPACTS[13],
        "keyword": IMPACT_KEYWORDS[1143]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1385]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[922]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1127]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1292]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1192]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1005]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1219]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1623]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2140]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1479]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[829]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[212]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1496]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[695]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1364]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1854]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[493]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[624]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2178]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2146]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[428]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[659]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1729]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[177]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[287]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1668]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[98]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[54]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[973]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1885]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1415]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[145]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[932]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[730]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2072]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1659]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1581]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1592]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1960]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[906]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[586]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1101]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[243]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[230]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[928]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[849]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[989]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1693]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[539]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[101]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1231]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2013]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[971]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[284]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[925]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[63]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1506]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[142]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1548]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1049]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[955]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1811]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[754]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1616]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[344]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2142]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[853]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1545]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[1016]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[2109]
    },
    {
        "impact": IMPACTS[14],
        "keyword": IMPACT_KEYWORDS[588]
    },
    {
        "impact": IMPACTS[15],
        "keyword": IMPACT_KEYWORDS[1166]
    },
    {
        "impact": IMPACTS[15],
        "keyword": IMPACT_KEYWORDS[550]
    },
    {
        "impact": IMPACTS[15],
        "keyword": IMPACT_KEYWORDS[1445]
    },
    {
        "impact": IMPACTS[15],
        "keyword": IMPACT_KEYWORDS[71]
    },
    {
        "impact": IMPACTS[15],
        "keyword": IMPACT_KEYWORDS[1896]
    },
    {
        "impact": IMPACTS[15],
        "keyword": IMPACT_KEYWORDS[1176]
    },
    {
        "impact": IMPACTS[16],
        "keyword": IMPACT_KEYWORDS[923]
    },
    {
        "impact": IMPACTS[16],
        "keyword": IMPACT_KEYWORDS[2055]
    },
    {
        "impact": IMPACTS[16],
        "keyword": IMPACT_KEYWORDS[1417]
    },
    {
        "impact": IMPACTS[16],
        "keyword": IMPACT_KEYWORDS[1125]
    },
    {
        "impact": IMPACTS[16],
        "keyword": IMPACT_KEYWORDS[1298]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[819]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1859]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1304]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1482]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1607]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[785]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1289]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1819]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1702]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1622]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[2105]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[516]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[572]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[2176]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[96]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[472]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[196]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1611]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1746]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1791]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[560]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[413]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[630]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1891]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[221]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[699]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1696]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1699]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[575]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1917]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[2190]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[380]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1646]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[147]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[1597]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[774]
    },
    {
        "impact": IMPACTS[17],
        "keyword": IMPACT_KEYWORDS[373]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[507]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1303]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[47]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1571]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1310]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[33]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1751]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1723]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[239]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1663]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[2193]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[490]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1603]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1095]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1979]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1505]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1170]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[1211]
    },
    {
        "impact": IMPACTS[18],
        "keyword": IMPACT_KEYWORDS[933]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1835]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1637]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1296]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[810]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[2090]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1043]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1194]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1182]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[138]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[6]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1624]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[725]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[426]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1105]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[2118]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[391]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1090]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[321]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[27]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[2070]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[482]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1983]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[558]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1106]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[1941]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[617]
    },
    {
        "impact": IMPACTS[19],
        "keyword": IMPACT_KEYWORDS[2106]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[206]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[330]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[195]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[451]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[2054]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[90]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[2220]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[662]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[2017]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[35]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[2032]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[871]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1401]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[2077]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[893]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1272]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1566]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[499]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[869]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[215]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[862]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1964]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[279]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1629]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[112]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1515]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1942]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1188]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1710]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[456]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[765]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1701]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[151]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1759]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[297]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1652]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1351]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1938]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1299]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[328]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1839]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1083]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1291]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[602]
    },
    {
        "impact": IMPACTS[20],
        "keyword": IMPACT_KEYWORDS[1452]
    },
    {
        "impact": IMPACTS[21],
        "keyword": IMPACT_KEYWORDS[65]
    },
    {
        "impact": IMPACTS[21],
        "keyword": IMPACT_KEYWORDS[915]
    },
    {
        "impact": IMPACTS[21],
        "keyword": IMPACT_KEYWORDS[873]
    },
    {
        "impact": IMPACTS[21],
        "keyword": IMPACT_KEYWORDS[1892]
    },
    {
        "impact": IMPACTS[22],
        "keyword": IMPACT_KEYWORDS[1334]
    },
    {
        "impact": IMPACTS[22],
        "keyword": IMPACT_KEYWORDS[1722]
    },
    {
        "impact": IMPACTS[22],
        "keyword": IMPACT_KEYWORDS[889]
    },
    {
        "impact": IMPACTS[22],
        "keyword": IMPACT_KEYWORDS[1433]
    },
    {
        "impact": IMPACTS[22],
        "keyword": IMPACT_KEYWORDS[299]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[283]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[1216]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[1523]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[250]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[1427]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[509]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[2043]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[809]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[867]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[310]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[387]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[2231]
    },
    {
        "impact": IMPACTS[23],
        "keyword": IMPACT_KEYWORDS[684]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1804]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[399]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[2016]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[895]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1258]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1626]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[2028]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1337]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[727]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[378]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[201]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[648]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[294]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1541]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[2014]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[2059]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1731]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1308]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[980]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1946]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1098]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[437]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1708]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1672]
    },
    {
        "impact": IMPACTS[24],
        "keyword": IMPACT_KEYWORDS[1232]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[1762]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[1716]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[1703]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[1357]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[1315]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[1797]
    },
    {
        "impact": IMPACTS[25],
        "keyword": IMPACT_KEYWORDS[729]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[504]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[626]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1108]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[526]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1156]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1901]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1051]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[540]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1841]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[563]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1963]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[0]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1991]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1311]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1517]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[2020]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[987]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1144]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1972]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1538]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[377]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[717]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1583]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1698]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[625]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[394]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[371]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1330]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1392]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[839]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[1857]
    },
    {
        "impact": IMPACTS[26],
        "keyword": IMPACT_KEYWORDS[2047]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[1406]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[1456]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[2068]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[1168]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[2229]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[1986]
    },
    {
        "impact": IMPACTS[27],
        "keyword": IMPACT_KEYWORDS[1745]
    },
    {
        "impact": IMPACTS[28],
        "keyword": IMPACT_KEYWORDS[1737]
    },
    {
        "impact": IMPACTS[28],
        "keyword": IMPACT_KEYWORDS[1074]
    },
    {
        "impact": IMPACTS[28],
        "keyword": IMPACT_KEYWORDS[1438]
    },
    {
        "impact": IMPACTS[28],
        "keyword": IMPACT_KEYWORDS[58]
    },
    {
        "impact": IMPACTS[29],
        "keyword": IMPACT_KEYWORDS[1380]
    },
    {
        "impact": IMPACTS[29],
        "keyword": IMPACT_KEYWORDS[580]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[263]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1664]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1403]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[757]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1596]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[435]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[885]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1263]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[153]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[478]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1549]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1248]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1150]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[812]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[2071]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1935]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[314]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1046]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[2183]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[609]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1632]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1913]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1220]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[2157]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1040]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[658]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[106]
    },
    {
        "impact": IMPACTS[30],
        "keyword": IMPACT_KEYWORDS[1976]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[958]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1129]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1205]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[848]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1882]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[479]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1246]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1332]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[483]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[247]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1490]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1783]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1206]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1681]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[2173]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1353]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1077]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1100]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1973]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[370]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1048]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1275]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[256]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1437]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1744]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[2197]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[2003]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1360]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[674]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[257]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1070]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[2034]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1249]
    },
    {
        "impact": IMPACTS[31],
        "keyword": IMPACT_KEYWORDS[1943]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[1044]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[537]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[598]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[1088]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[1542]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[1674]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[1955]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[1447]
    },
    {
        "impact": IMPACTS[32],
        "keyword": IMPACT_KEYWORDS[222]
    },
    {
        "impact": IMPACTS[33],
        "keyword": IMPACT_KEYWORDS[1876]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[775]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1593]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1772]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1222]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1767]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1278]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[253]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[930]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1394]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[91]
    },
    {
        "impact": IMPACTS[34],
        "keyword": IMPACT_KEYWORDS[1771]
    },
    {
        "impact": IMPACTS[35],
        "keyword": IMPACT_KEYWORDS[1230]
    },
    {
        "impact": IMPACTS[35],
        "keyword": IMPACT_KEYWORDS[129]
    },
    {
        "impact": IMPACTS[35],
        "keyword": IMPACT_KEYWORDS[489]
    },
    {
        "impact": IMPACTS[35],
        "keyword": IMPACT_KEYWORDS[242]
    },
    {
        "impact": IMPACTS[35],
        "keyword": IMPACT_KEYWORDS[365]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[657]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1528]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[665]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[2184]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[2217]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[981]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1520]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1032]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[916]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[2145]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1749]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1614]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[289]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1658]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[326]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[32]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1250]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[301]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1462]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[638]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[2078]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[136]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1224]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1689]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1714]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1449]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[2164]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1997]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[369]
    },
    {
        "impact": IMPACTS[36],
        "keyword": IMPACT_KEYWORDS[1747]
    },
    {
        "impact": IMPACTS[37],
        "keyword": IMPACT_KEYWORDS[907]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[1802]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[2191]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[970]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[636]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[603]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[914]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[796]
    },
    {
        "impact": IMPACTS[38],
        "keyword": IMPACT_KEYWORDS[49]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[2112]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[948]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[2107]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[1195]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[2081]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[1875]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[439]
    },
    {
        "impact": IMPACTS[39],
        "keyword": IMPACT_KEYWORDS[2195]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[1114]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[1495]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[97]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[1855]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[150]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[5]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[234]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[60]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[467]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[401]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[1752]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[2000]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[622]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[1302]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[187]
    },
    {
        "impact": IMPACTS[40],
        "keyword": IMPACT_KEYWORDS[880]
    },
    {
        "impact": IMPACTS[41],
        "keyword": IMPACT_KEYWORDS[1633]
    },
    {
        "impact": IMPACTS[41],
        "keyword": IMPACT_KEYWORDS[152]
    },
    {
        "impact": IMPACTS[41],
        "keyword": IMPACT_KEYWORDS[733]
    },
    {
        "impact": IMPACTS[41],
        "keyword": IMPACT_KEYWORDS[1431]
    },
    {
        "impact": IMPACTS[41],
        "keyword": IMPACT_KEYWORDS[449]
    },
    {
        "impact": IMPACTS[41],
        "keyword": IMPACT_KEYWORDS[2185]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1229]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1682]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[42]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1321]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1539]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1687]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[887]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[707]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[141]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[947]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[2018]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1884]
    },
    {
        "impact": IMPACTS[42],
        "keyword": IMPACT_KEYWORDS[1650]
    },
    {
        "impact": IMPACTS[43],
        "keyword": IMPACT_KEYWORDS[182]
    },
    {
        "impact": IMPACTS[43],
        "keyword": IMPACT_KEYWORDS[1151]
    },
    {
        "impact": IMPACTS[43],
        "keyword": IMPACT_KEYWORDS[2202]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[1500]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[1476]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[995]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[1370]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[934]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[728]
    },
    {
        "impact": IMPACTS[44],
        "keyword": IMPACT_KEYWORDS[988]
    },
    {
        "impact": IMPACTS[45],
        "keyword": IMPACT_KEYWORDS[67]
    },
    {
        "impact": IMPACTS[45],
        "keyword": IMPACT_KEYWORDS[1862]
    },
    {
        "impact": IMPACTS[45],
        "keyword": IMPACT_KEYWORDS[1474]
    },
    {
        "impact": IMPACTS[45],
        "keyword": IMPACT_KEYWORDS[1738]
    },
    {
        "impact": IMPACTS[45],
        "keyword": IMPACT_KEYWORDS[1293]
    },
    {
        "impact": IMPACTS[46],
        "keyword": IMPACT_KEYWORDS[2108]
    },
    {
        "impact": IMPACTS[46],
        "keyword": IMPACT_KEYWORDS[88]
    },
    {
        "impact": IMPACTS[46],
        "keyword": IMPACT_KEYWORDS[1742]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[854]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[1965]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[1966]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[156]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[897]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[1067]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[542]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[400]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[2110]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[185]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[1956]
    },
    {
        "impact": IMPACTS[47],
        "keyword": IMPACT_KEYWORDS[623]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1124]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1792]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1450]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[406]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[910]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1670]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[993]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[431]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1494]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[731]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[46]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1165]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1550]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1981]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[878]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1268]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1724]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1850]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1789]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[209]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2223]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[874]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1773]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1240]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2218]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[994]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[719]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2121]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[541]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1643]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1472]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1073]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[255]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2208]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[600]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[860]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1227]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1345]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1313]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1911]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1720]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[639]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[961]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[464]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2200]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[566]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1475]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[687]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1544]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[940]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[286]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1547]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1178]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2194]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[752]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[698]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[718]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1085]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1971]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1649]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1739]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1897]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1399]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[891]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1287]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[652]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[587]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1093]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[571]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[813]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[592]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[972]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1208]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1513]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1020]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1830]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1323]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1790]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1314]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[999]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[990]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1572]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1907]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[943]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1757]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2092]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1813]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[395]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2125]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1992]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1735]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[420]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1778]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[708]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[171]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1384]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[2226]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1898]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[347]
    },
    {
        "impact": IMPACTS[48],
        "keyword": IMPACT_KEYWORDS[1502]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[803]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[204]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[2101]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1079]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1448]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[322]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[2051]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1644]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[461]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[795]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[166]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1636]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[2162]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[417]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[223]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[548]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1886]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1625]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[2075]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1157]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[2149]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1785]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[12]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[388]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[416]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1147]
    },
    {
        "impact": IMPACTS[49],
        "keyword": IMPACT_KEYWORDS[1918]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[1967]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[534]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[805]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[771]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[51]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[935]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[179]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[358]
    },
    {
        "impact": IMPACTS[50],
        "keyword": IMPACT_KEYWORDS[25]
    },
    {
        "impact": IMPACTS[51],
        "keyword": IMPACT_KEYWORDS[1927]
    },
    {
        "impact": IMPACTS[51],
        "keyword": IMPACT_KEYWORDS[1365]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1557]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[238]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1577]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1763]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[10]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[374]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[2166]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[15]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[502]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1338]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1130]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1760]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1989]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[619]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1136]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[414]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1508]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[2064]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[491]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1732]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1707]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1864]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[312]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[356]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1558]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[2153]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[389]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1223]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[190]
    },
    {
        "impact": IMPACTS[52],
        "keyword": IMPACT_KEYWORDS[1916]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[653]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1677]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[735]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[902]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1324]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[2204]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1921]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[323]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1577]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[123]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[2166]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[468]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[2124]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[610]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1235]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1338]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1130]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1760]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1989]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1136]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[671]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1508]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1707]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[208]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[2080]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[312]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[2026]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1558]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[984]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[2168]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[61]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1223]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[190]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1567]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[884]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[114]
    },
    {
        "impact": IMPACTS[53],
        "keyword": IMPACT_KEYWORDS[1916]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[466]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[782]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[341]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[78]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[300]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1931]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[787]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1826]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[721]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[118]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[161]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[43]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[2211]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1487]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[2154]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1348]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1930]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1340]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[858]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[1072]
    },
    {
        "impact": IMPACTS[54],
        "keyword": IMPACT_KEYWORDS[620]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1346]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1356]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1594]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1697]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[2135]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[2082]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[224]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1218]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1256]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[429]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[16]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[199]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[553]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1799]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[2022]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[226]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1468]
    },
    {
        "impact": IMPACTS[55],
        "keyword": IMPACT_KEYWORDS[1060]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1669]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1346]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1017]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1478]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[176]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[768]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2007]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1748]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2117]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1519]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1697]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1430]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[92]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[946]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[847]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[753]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[832]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1606]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[350]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[342]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1845]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1497]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1562]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1361]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1382]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1259]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[108]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1389]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[275]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1091]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[846]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[24]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1381]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1608]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[668]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[404]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[826]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1536]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[501]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[127]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2139]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[949]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1424]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[693]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[875]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2187]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1210]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1725]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1169]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1796]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[577]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1863]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[599]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2104]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2148]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1846]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1507]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[9]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1377]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1164]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[74]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[529]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2015]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[531]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[333]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1373]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[132]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[711]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1212]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[722]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[697]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2225]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1080]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[635]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[2175]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[569]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1712]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1904]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1131]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[315]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[313]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[481]
    },
    {
        "impact": IMPACTS[56],
        "keyword": IMPACT_KEYWORDS[1197]
    },
    {
        "impact": IMPACTS[57],
        "keyword": IMPACT_KEYWORDS[1061]
    },
    {
        "impact": IMPACTS[57],
        "keyword": IMPACT_KEYWORDS[444]
    },
    {
        "impact": IMPACTS[57],
        "keyword": IMPACT_KEYWORDS[788]
    },
    {
        "impact": IMPACTS[57],
        "keyword": IMPACT_KEYWORDS[883]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[937]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[1870]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[1458]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[1591]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[117]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[103]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[2100]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[545]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[554]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[779]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[1411]
    },
    {
        "impact": IMPACTS[58],
        "keyword": IMPACT_KEYWORDS[1414]
    },
    {
        "impact": IMPACTS[59],
        "keyword": IMPACT_KEYWORDS[1152]
    },
    {
        "impact": IMPACTS[59],
        "keyword": IMPACT_KEYWORDS[1831]
    },
    {
        "impact": IMPACTS[59],
        "keyword": IMPACT_KEYWORDS[1185]
    },
    {
        "impact": IMPACTS[59],
        "keyword": IMPACT_KEYWORDS[338]
    },
    {
        "impact": IMPACTS[59],
        "keyword": IMPACT_KEYWORDS[952]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[2120]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[670]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[188]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[751]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[99]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[1288]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[183]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[334]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[1034]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[4]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[2052]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[1214]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[126]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[244]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[1025]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[296]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[1009]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[629]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[1499]
    },
    {
        "impact": IMPACTS[60],
        "keyword": IMPACT_KEYWORDS[415]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[881]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1801]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1902]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[271]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[488]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[2085]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[492]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[432]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[2169]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[109]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[331]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1137]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[797]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[345]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1741]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[568]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[292]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[57]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[336]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1344]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[812]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1347]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1243]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1935]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[857]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[594]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[709]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1086]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1786]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[523]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1537]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[2183]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[87]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1109]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[14]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[800]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[167]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[533]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[565]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[845]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1470]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1247]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[75]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1888]
    },
    {
        "impact": IMPACTS[61],
        "keyword": IMPACT_KEYWORDS[1939]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[881]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1801]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1902]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1403]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[271]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2085]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[492]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[435]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1004]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[153]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1586]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[432]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2169]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1209]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[596]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1159]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[835]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[528]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[109]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[331]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1137]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1549]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1244]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1248]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[268]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[797]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1807]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1055]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[345]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2192]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1741]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[568]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[292]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[135]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[336]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[513]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1344]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[812]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1491]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2071]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1347]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1488]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1463]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1243]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1935]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1883]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[346]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1719]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1919]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[857]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1309]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[398]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[594]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1776]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[709]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1086]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2221]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1786]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[523]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2006]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1407]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1537]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2183]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[447]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1982]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1062]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[87]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1109]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[649]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1996]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[14]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1220]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[800]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[55]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[290]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[167]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[533]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[565]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[845]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[139]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1039]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1470]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1865]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[747]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[842]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2053]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[776]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[676]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[2093]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1726]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1953]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1247]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1350]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1915]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1040]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[75]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[106]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1084]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1975]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[756]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1888]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1112]
    },
    {
        "impact": IMPACTS[62],
        "keyword": IMPACT_KEYWORDS[1939]
    },
    {
        "impact": IMPACTS[63],
        "keyword": IMPACT_KEYWORDS[2029]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[2131]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[2152]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[1321]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[678]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[1539]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[1687]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[827]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[779]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[1037]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[821]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[947]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[1650]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[1404]
    },
    {
        "impact": IMPACTS[64],
        "keyword": IMPACT_KEYWORDS[834]
    },
    {
        "impact": IMPACTS[65],
        "keyword": IMPACT_KEYWORDS[1171]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[742]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[1782]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[137]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[375]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[546]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[579]
    },
    {
        "impact": IMPACTS[66],
        "keyword": IMPACT_KEYWORDS[1285]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[396]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1784]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1187]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1877]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[611]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[159]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[207]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1878]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1844]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1018]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[52]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1096]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[791]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[739]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1320]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[634]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[217]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1665]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1145]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1639]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[332]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[991]
    },
    {
        "impact": IMPACTS[67],
        "keyword": IMPACT_KEYWORDS[1526]
    },
    {
        "impact": IMPACTS[68],
        "keyword": IMPACT_KEYWORDS[277]
    },
    {
        "impact": IMPACTS[68],
        "keyword": IMPACT_KEYWORDS[1803]
    },
    {
        "impact": IMPACTS[68],
        "keyword": IMPACT_KEYWORDS[1273]
    },
    {
        "impact": IMPACTS[68],
        "keyword": IMPACT_KEYWORDS[7]
    },
    {
        "impact": IMPACTS[69],
        "keyword": IMPACT_KEYWORDS[1683]
    },
    {
        "impact": IMPACTS[69],
        "keyword": IMPACT_KEYWORDS[544]
    },
    {
        "impact": IMPACTS[69],
        "keyword": IMPACT_KEYWORDS[376]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[532]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2009]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[801]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1383]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[259]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1766]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1300]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1113]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[601]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[543]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1860]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1180]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[269]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2133]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1934]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2044]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1944]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1627]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2027]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2088]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[870]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1816]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[669]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[363]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2165]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1514]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2031]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[692]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[339]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2058]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1286]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1092]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1861]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1709]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1535]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1685]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2198]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2136]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[298]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1641]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2147]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1295]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[746]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[494]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1002]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1753]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[53]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[2159]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[641]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[353]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[645]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[831]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1949]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1167]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[518]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1241]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1102]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1262]
    },
    {
        "impact": IMPACTS[70],
        "keyword": IMPACT_KEYWORDS[1568]
    },
    {
        "impact": IMPACTS[71],
        "keyword": IMPACT_KEYWORDS[1064]
    },
    {
        "impact": IMPACTS[71],
        "keyword": IMPACT_KEYWORDS[1434]
    },
    {
        "impact": IMPACTS[71],
        "keyword": IMPACT_KEYWORDS[2155]
    },
    {
        "impact": IMPACTS[72],
        "keyword": IMPACT_KEYWORDS[1933]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1937]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1768]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1828]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1237]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1274]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[892]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[29]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[85]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[497]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1056]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[2163]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1809]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1123]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1352]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[741]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1525]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[863]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1408]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1994]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1396]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[547]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[229]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1158]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1027]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[2063]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1727]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1924]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[149]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[368]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[535]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[525]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1853]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[613]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[262]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[170]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[282]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1342]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1540]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[249]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[737]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[438]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1524]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1081]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1239]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[498]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1329]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1006]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[685]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[440]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1146]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[169]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[758]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[944]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[448]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[143]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1825]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[458]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1111]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[696]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[608]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1179]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[120]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1945]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1587]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[683]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1881]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[37]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[784]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[772]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1798]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[631]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1000]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1203]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[19]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1821]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[794]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1995]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1653]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[521]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[1666]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[789]
    },
    {
        "impact": IMPACTS[73],
        "keyword": IMPACT_KEYWORDS[2156]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1635]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1132]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1120]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1429]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[80]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[549]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2004]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1305]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[597]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[690]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1455]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[443]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1769]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[992]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[817]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1805]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1446]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[245]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[162]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1838]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1031]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1428]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1512]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2170]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[633]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[320]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[605]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[799]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1909]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1951]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1777]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[258]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2215]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[81]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[807]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[302]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2073]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[660]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1822]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1501]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[773]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1198]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[734]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1612]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[73]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1028]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[655]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1260]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[920]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1806]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1184]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2182]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1153]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1306]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[637]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[231]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[536]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[744]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[86]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1920]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1154]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1270]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1001]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[938]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2102]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1578]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[246]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[442]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[116]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[2050]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1978]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[859]
    },
    {
        "impact": IMPACTS[74],
        "keyword": IMPACT_KEYWORDS[1764]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[804]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[2179]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[267]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[589]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[2097]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[581]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1552]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[2040]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[265]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[815]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1190]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1024]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[978]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1280]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1319]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[44]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1104]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1379]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[909]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[786]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[1657]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[213]
    },
    {
        "impact": IMPACTS[75],
        "keyword": IMPACT_KEYWORDS[816]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[524]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[178]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1065]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1266]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[974]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[968]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1609]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[165]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1833]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1648]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[455]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1473]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2213]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1485]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1543]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1467]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[76]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[317]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1457]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[471]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1294]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2083]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1054]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1705]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1128]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[562]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1267]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1161]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2113]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1814]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[192]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[45]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[307]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[798]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[913]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2076]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[654]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1590]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[364]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1489]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[351]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[559]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1779]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1503]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1442]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[111]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[673]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[898]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[879]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1974]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[251]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2008]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1251]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[293]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2048]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[661]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1174]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1148]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[220]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[23]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1820]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[496]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[713]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2042]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[366]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[115]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1134]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[682]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2137]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1225]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[764]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1840]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1498]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[421]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1950]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[663]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[157]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[430]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[745]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1045]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[2199]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[830]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1252]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1010]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1988]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[79]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1139]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[180]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1255]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1842]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1362]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[702]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1615]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[140]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1021]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1619]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[405]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[174]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[1754]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[720]
    },
    {
        "impact": IMPACTS[76],
        "keyword": IMPACT_KEYWORDS[582]
    },
    {
        "impact": IMPACTS[77],
        "keyword": IMPACT_KEYWORDS[360]
    },
    {
        "impact": IMPACTS[77],
        "keyword": IMPACT_KEYWORDS[1116]
    },
    {
        "impact": IMPACTS[77],
        "keyword": IMPACT_KEYWORDS[1047]
    },
    {
        "impact": IMPACTS[78],
        "keyword": IMPACT_KEYWORDS[327]
    },
    {
        "impact": IMPACTS[78],
        "keyword": IMPACT_KEYWORDS[272]
    },
    {
        "impact": IMPACTS[78],
        "keyword": IMPACT_KEYWORDS[393]
    },
    {
        "impact": IMPACTS[78],
        "keyword": IMPACT_KEYWORDS[627]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[2207]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[2023]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[1440]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[755]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[1788]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[1412]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[1836]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[1282]
    },
    {
        "impact": IMPACTS[79],
        "keyword": IMPACT_KEYWORDS[2045]
    },
    {
        "impact": IMPACTS[80],
        "keyword": IMPACT_KEYWORDS[646]
    },
    {
        "impact": IMPACTS[80],
        "keyword": IMPACT_KEYWORDS[667]
    },
    {
        "impact": IMPACTS[80],
        "keyword": IMPACT_KEYWORDS[1847]
    },
    {
        "impact": IMPACTS[81],
        "keyword": IMPACT_KEYWORDS[1368]
    },
    {
        "impact": IMPACTS[81],
        "keyword": IMPACT_KEYWORDS[2084]
    },
    {
        "impact": IMPACTS[81],
        "keyword": IMPACT_KEYWORDS[979]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1008]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1469]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[2177]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1504]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1868]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1529]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[985]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[383]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[2024]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1191]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1386]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1694]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1465]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[2172]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1418]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1328]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1579]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[308]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[425]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[1026]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[917]
    },
    {
        "impact": IMPACTS[82],
        "keyword": IMPACT_KEYWORDS[362]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1610]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1849]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[181]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[232]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1163]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1867]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[647]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[477]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1869]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[197]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1647]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1410]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1817]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[584]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1234]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[2041]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[868]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[390]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[64]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[311]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[2128]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[486]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[956]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1422]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1118]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[340]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1012]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[2111]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1516]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[500]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[900]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1984]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[2224]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[2209]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1322]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1325]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[418]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[476]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[957]
    },
    {
        "impact": IMPACTS[83],
        "keyword": IMPACT_KEYWORDS[1071]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[335]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[441]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[732]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[113]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[966]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[615]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1029]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[2005]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[2158]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[778]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1014]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1852]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1149]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1812]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1326]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[527]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1271]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1667]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1181]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1269]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1461]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[781]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[780]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1700]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[459]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1115]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1926]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[640]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1531]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1690]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1715]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[484]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[632]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[820]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[288]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[386]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1460]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1372]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1200]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[2134]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1574]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1349]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[564]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[384]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[2099]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1818]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[643]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[228]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1815]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[929]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1030]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[614]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1661]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[899]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1756]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1063]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1588]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1595]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[2160]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[381]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[475]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1660]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[202]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1957]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[505]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[522]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[20]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1432]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[1679]
    },
    {
        "impact": IMPACTS[84],
        "keyword": IMPACT_KEYWORDS[574]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[113]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1602]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[615]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1228]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[48]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[2196]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[422]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1053]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[726]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1019]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1484]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[291]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1213]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1667]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1453]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[865]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1932]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[357]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[2115]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[459]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[172]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[621]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1460]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1761]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[8]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1675]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[407]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1704]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[191]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[688]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1600]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[228]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[929]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[372]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[556]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1661]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1893]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1138]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[769]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[446]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1142]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1172]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[888]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1097]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1957]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[950]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[618]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[864]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[715]
    },
    {
        "impact": IMPACTS[85],
        "keyword": IMPACT_KEYWORDS[1605]
    },
    {
        "impact": IMPACTS[86],
        "keyword": IMPACT_KEYWORDS[1728]
    },
    {
        "impact": IMPACTS[87],
        "keyword": IMPACT_KEYWORDS[921]
    },
    {
        "impact": IMPACTS[87],
        "keyword": IMPACT_KEYWORDS[2019]
    },
    {
        "impact": IMPACTS[87],
        "keyword": IMPACT_KEYWORDS[951]
    },
    {
        "impact": IMPACTS[87],
        "keyword": IMPACT_KEYWORDS[520]
    },
    {
        "impact": IMPACTS[87],
        "keyword": IMPACT_KEYWORDS[1556]
    },
    {
        "impact": IMPACTS[87],
        "keyword": IMPACT_KEYWORDS[761]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[664]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[1580]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[203]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[273]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[1435]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[1993]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[474]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[2011]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[1848]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[1066]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[2035]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[918]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[1413]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[877]
    },
    {
        "impact": IMPACTS[88],
        "keyword": IMPACT_KEYWORDS[2046]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2060]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[158]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[508]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[886]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[21]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1733]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1493]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1155]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[759]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[712]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2126]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1199]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1673]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[59]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[409]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2021]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2012]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[39]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[94]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[691]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1671]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[266]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[680]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[237]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2222]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[62]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1466]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[823]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1202]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2189]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1162]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1387]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[236]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[704]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[760]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[561]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1879]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1007]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[591]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2122]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2210]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[56]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1119]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[942]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1443]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[538]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[656]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[309]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[324]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2079]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[616]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[642]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1522]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[710]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1436]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1405]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[211]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1620]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[872]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[349]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[967]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1022]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[969]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[133]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2129]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[270]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[2171]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[316]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1395]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[551]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[278]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1050]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1099]
    },
    {
        "impact": IMPACTS[89],
        "keyword": IMPACT_KEYWORDS[1126]
    },
    {
        "impact": IMPACTS[90],
        "keyword": IMPACT_KEYWORDS[1676]
    },
    {
        "impact": IMPACTS[90],
        "keyword": IMPACT_KEYWORDS[506]
    },
    {
        "impact": IMPACTS[90],
        "keyword": IMPACT_KEYWORDS[856]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[260]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1718]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[216]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[36]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1824]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[681]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1894]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[962]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1617]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1655]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[392]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1968]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[2141]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1301]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[2212]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[34]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[700]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1089]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[901]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1425]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[740]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1355]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[2095]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1793]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1110]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1133]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[359]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1367]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[2181]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[184]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[31]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[954]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[2091]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[419]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1546]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1236]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1706]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1563]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1787]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[998]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[252]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1290]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1765]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1795]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[828]
    },
    {
        "impact": IMPACTS[91],
        "keyword": IMPACT_KEYWORDS[1117]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[894]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2132]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[248]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1723]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[762]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1477]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[434]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[965]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[511]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1068]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2002]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[882]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1827]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1451]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1238]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2089]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1645]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[276]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[666]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[355]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[423]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1740]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2074]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[352]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[725]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[650]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[361]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1393]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1307]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2038]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[840]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1640]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[321]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2103]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2214]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[2070]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1059]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1193]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1207]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[427]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[367]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1312]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1905]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[200]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[590]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1211]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1837]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[18]
    },
    {
        "impact": IMPACTS[92],
        "keyword": IMPACT_KEYWORDS[1621]
    },
    {
        "impact": IMPACTS[93],
        "keyword": IMPACT_KEYWORDS[408]
    },
    {
        "impact": IMPACTS[93],
        "keyword": IMPACT_KEYWORDS[1082]
    },
    {
        "impact": IMPACTS[93],
        "keyword": IMPACT_KEYWORDS[325]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[1335]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[2116]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[1900]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[1887]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[679]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[274]
    },
    {
        "impact": IMPACTS[94],
        "keyword": IMPACT_KEYWORDS[964]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1781]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1912]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[851]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1980]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[186]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[235]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[792]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[585]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1977]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[210]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[379]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[996]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1906]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1560]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1565]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1895]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1464]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1750]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1940]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[802]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[519]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1177]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2057]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1533]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1510]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1264]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1630]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[578]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1829]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[926]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2094]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1834]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[606]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1317]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[705]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[50]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1058]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[411]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1601]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[402]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[463]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[473]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1471]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1948]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[716]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2096]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[304]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2186]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1420]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[844]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[777]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1866]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2143]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1297]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1035]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[552]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1662]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[303]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[890]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[40]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1441]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1570]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[843]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1400]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2227]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1910]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[841]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[77]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[175]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[130]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1003]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1366]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[205]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[30]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1903]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1899]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[28]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[412]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1990]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2114]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[850]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[119]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1642]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1354]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1376]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[607]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[738]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1013]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[264]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[144]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[866]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[824]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[570]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[672]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[436]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2049]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2061]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1015]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[154]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1730]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1343]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1135]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[808]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[17]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[701]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1743]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[838]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1339]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2230]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[783]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[41]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1613]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[485]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1284]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1189]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[517]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[125]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1374]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1261]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1952]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1534]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[694]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1575]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1036]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[241]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2056]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1221]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[896]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1962]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[70]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1121]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[595]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1421]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[919]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[319]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[457]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1011]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[555]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[975]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2167]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1923]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1678]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1041]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1794]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2201]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[385]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2205]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1042]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1604]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[793]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[66]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1388]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2206]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1518]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2098]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1245]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[822]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[736]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1217]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[93]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1599]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1075]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[38]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[743]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[833]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[460]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1925]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[677]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[403]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[515]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1402]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[89]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1872]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1391]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[567]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1961]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[576]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1987]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1688]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[960]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[433]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1734]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[168]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[530]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1598]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1279]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[69]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[814]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[295]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[382]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1711]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1201]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[410]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1492]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1691]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[2119]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[68]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[233]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[1369]
    },
    {
        "impact": IMPACTS[95],
        "keyword": IMPACT_KEYWORDS[836]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[1569]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[173]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[1276]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[305]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[1554]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[1686]
    },
    {
        "impact": IMPACTS[96],
        "keyword": IMPACT_KEYWORDS[193]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[218]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[480]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1908]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[219]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1628]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[876]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[104]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1775]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[651]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[163]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[557]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1242]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[912]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1589]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[911]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[604]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[2066]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[3]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[628]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1770]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[285]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[124]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1233]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1511]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1057]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[26]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1928]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[749]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[348]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[2033]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1527]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[908]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1107]
    },
    {
        "impact": IMPACTS[97],
        "keyword": IMPACT_KEYWORDS[1721]
    },
    {
        "impact": IMPACTS[98],
        "keyword": IMPACT_KEYWORDS[1141]
    },
    {
        "impact": IMPACTS[98],
        "keyword": IMPACT_KEYWORDS[450]
    },
    {
        "impact": IMPACTS[98],
        "keyword": IMPACT_KEYWORDS[593]
    },
    {
        "impact": IMPACTS[99],
        "keyword": IMPACT_KEYWORDS[1532]
    },
    {
        "impact": IMPACTS[99],
        "keyword": IMPACT_KEYWORDS[1423]
    },
    {
        "impact": IMPACTS[99],
        "keyword": IMPACT_KEYWORDS[343]
    },
    {
        "impact": IMPACTS[99],
        "keyword": IMPACT_KEYWORDS[1874]
    },
    {
        "impact": IMPACTS[99],
        "keyword": IMPACT_KEYWORDS[337]
    }
]


def populate_impacts(apps, schema_editor):
    Impact = apps.get_model('core', 'Impact')
    Impact.objects.all().delete()
    Impact.objects.bulk_create([Impact(**impact) for impact in IMPACTS])


def populate_impact_keywords(apps, schema_editor):
    ImpactKeyword = apps.get_model('core', 'ImpactKeyword')
    ImpactKeyword.objects.all().delete()
    ImpactKeyword.objects.bulk_create([ImpactKeyword(**keyword) for keyword in IMPACT_KEYWORDS])


def populate_impact_keywords_m2m(apps, schema_editor):
    ImpactKeyword = apps.get_model('core', 'ImpactKeyword')
    Impact = apps.get_model('core', 'Impact')
    Through = Impact.keywords.through
    Through.objects.all().delete()
    for impact_keyword_m2m in IMPACT_KEYWORDS_M2M:
        impact = Impact.objects.get(**impact_keyword_m2m.pop('impact'))
        keyword = ImpactKeyword.objects.get(**impact_keyword_m2m.pop('keyword'))
        Through.objects.create(**impact_keyword_m2m, impact=impact, impactkeyword=keyword)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20210722_1049'),
    ]

    operations = [
        migrations.RunPython(populate_impacts),
        migrations.RunPython(populate_impact_keywords),
        migrations.RunPython(populate_impact_keywords_m2m),
    ]
