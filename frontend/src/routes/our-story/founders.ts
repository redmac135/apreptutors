type FounderProfile = {
    name: string;
    position: string;
    specialties: string[];
    university: string;
    photo?: string;
}

const PHOTO_PATH = "images/headshots/";

export const DEFAULT_PHOTO = PHOTO_PATH + "default.jpg";

export const FOUNDERS: FounderProfile[] = [
    {
        name: "Jedidiah Mao",
        position: "Curriculum Head",
        specialties: ["HL Physics", "SL French", "SL Chemistry"],
        university: "Integrated Biomedical Engineering & Health Sciences (iBioMed) @ McMaster",
        photo: PHOTO_PATH + "jedidiah.jpg"
    },
    {
        name: "Joanna Wang",
        position: "Curriculum Head",
        specialties: ["HL Chemistry", "HL Biology", "HL English"],
        university: "Financial Analysis and Risk Management @ Waterloo",
        photo: PHOTO_PATH + "joanna.jpg"
    },
    {
        name: "Ethan Zhao",
        position: "Curriculum Head, Web Developer",
        specialties: ["HL Physics", "HL Math"],
        university: "Ivey & Engineering @ Western",
        photo: PHOTO_PATH + "ethan.jpg"
    },
    {
        name: "Bryan Deng",
        position: "Curriculum Head, Web Developer",
        specialties: ["HL Physics", "HL Math"],
        university: "Computer Science @ Waterloo",
        photo: PHOTO_PATH + "bryan.png"
    }
]