import streamlit as st

def page1():
        st.header('Car Type')
        st.subheader('1. ซีดาน (Sedan)')
        st.markdown('ป็นหนึ่งในโมเดลที่คุ้นหน้าคุ้นตามากที่สุดในฐานะรถครอบครัวขนาดกะทัดรัด โดยจุดเด่นของรถรุ่นนี้คือ เป็นรถตัวถัง 4 ประตู และมีโซนสำหรับห้องสัมภาระท้ายใต้กระจกด้านหลังที่แยกจากกัน ตัวถังจะมีขนาดที่หลากหลาย และครอบคลุมทั้งรถธรรมดาจนถึงรถหรู ซึ่งคนไทยจะเรียกรถประเภทนี้ว่ารถเก๋ง ตัวอย่างของรถซีดาน อาทิ Honda City, Toyota Vios, Honda Civic, Toyota Camry และ Honda Accord')
        st.subheader('2. แฮตช์แบ็ก (Hatchback)')
        st.markdown('เป็นรถยนต์นั่งที่มีลักษณะคล้ายกับรถซีดาน แต่มีช่วงท้ายที่สั้น หรือที่เรียกกันว่าท้ายตัด มีทั้งรุ่น 3 ประตู และ 5 ประตู โดยนับจากประตูด้านข้างซ้าย-ขวา และฝากระโปรงหลังเป็นอีก 1 ประตู รถประเภทนี้จะใช้พื้นฐานร่วมกับรถตัวถังซีดาน นอกจากนี้ตัวรถมีพื้นที่บรรจุสัมภาระด้านท้ายได้มากขึ้น อีกทั้งอาจจะสามารถพับเบาะแถวสองของรถเพื่อเพิ่มพื้นที่อีกด้วย โดยรถในรูปแบบนี้จะครอบคลุมตั้งแต่รถธรรมดาจนถึงรถหรู อาทิ Mazda2, Toyota Yaris GR Sport, Honda Civic Hatchback และ Audi A3')
        st.subheader('3. สเตชั่นแวกอน (Station Wagon)')
        st.markdown('เป็นรถที่มีความคล้ายกับรถแฮตช์แบ็ก โดยจะมีส่วนท้ายที่ยื่นยาวมากกว่า สำหรับรองรับการบรรทุกสัมภาระ พร้อมกับถูกออกแบบเพิ่มจำนวนเสาของตัวรถ หรือที่เรียกว่าเสา D เพิ่มเข้ามา เพื่อให้มีพื้นที่โดยสาร หรือเก็บสัมภาระมากขึ้น รถแบบนี้เป็นรถที่ได้รับความนิยมในฐานะรถครอบครัวก่อนที่รถประเภทเอสยูวีจะมาครองตลาดแทนที่ โดยรถในกลุ่มนี้ในตลาดบ้านเราจะมี MG EP ที่มาในรูปแบบรถยนต์ไฟฟ้า, Mercedes-Benz E-Class Estate และ Subaru Outback')
        st.subheader('4. คูเป้ (Coupe)')
        st.markdown('สำหรับรถประเภทนี้จะเป็นรถ 2 ประตู พร้อมหลังคาที่ออกแบบให้ลาดท้าย ส่วนภายในจะมีให้เลือกทั้งแบบ 2 ที่นั่ง หรือ 4 ที่นั่ง ตามขนาดตัวถัง ส่วนมากจะพบได้ในกลุ่มรถสปอร์ต อาทิ Toyota GR86, Ford Mustang, Porsche Boxster แต่ในปัจจุบันครอบคลุมไปยังรถ 4 ประตู หลังคาท้ายลาด หรือเอสยูวีหลังคาท้ายลาด ที่ให้ลุคสปอร์ต อาทิ MG5, Mercedes-Benz CLS และ BMW X6 SUV')
        st.subheader('5. ครอสโอเวอร์ (Crossover)')
        st.markdown('รถประเภทครอสโอเวอร์หรือที่เรียกย่อ ๆ ว่ารถ CUV ที่ย่อมาจาก Crossover Utility Vehicle เป็นรถที่ถูกสร้างขึ้นบนโครงสร้างตัวถังแบบ Unibody หรือแชสซีส์และตัวถังเป็นชิ้นเดียวกัน หรือจะเรียกว่าเป็นการนำพื้นฐานของรถซีดานแล้วมาขยายร่างยกสูงขึ้น ซึ่งจะทำให้ตัวรถนั้นสามารถใช้งานได้หลากหลายขึ้น ลุยในเส้นทางที่รถซีดานหรือรถเก๋งธรรมดาเข้าไม่ถึง อีกทั้งยังเพิ่มในส่วนพื้นที่เก็บของได้มากกว่ารถซีดานทั่วไป โดยรถในกลุ่มนี้ก็จะมี Subaru XV EyeSight, Nissan Kicks เป็นต้น')
        st.subheader('6. รถเอสยูวี (SUV)')
        st.markdown('รถอเนกประสงค์ SUV (Sport Utility Vehicle) ซึ่งความหมายก็จะตรงตัวตามภาษาอังกฤษ ที่หมายความว่ารถอเนกประสงค์สารพัดประโยชน์ที่มีสมรรถนะสูง โดยจะเป็นรถที่มาในรูปแบบตัวถังขนาดใหญ่ ออกแบบมาเพื่อการใช้งานที่หลากหลาย มาพร้อมความสวยงาม ความสปอร์ต ในพื้นฐานของรถยนต์นั่งทั่วไป เหมาะกับครอบครัวที่มีขนาดใหญ่ที่ต้องการใช้พื้นที่ในรถยนต์อย่างกว้างขวาง มาพร้อมระบบขับเคลื่อน 4 ล้อ และ 2 ล้อ ซึ่งปัจจุบันกระแสของรถประเภท SUV กำลังได้รับความนิยมเป็นอย่างมาก โดยหากจะพูดถึง SUV ในบ้านเราจะมี Honda CR-V, Toyota C-HR, MG HS และ Mazda CX-5')
        st.subheader('7. รถกระบะ (Pickup)')
        st.markdown('รถกระบะ หรือรถปิกอัพ รถประเภทนี้จะมีเอกลักษณ์เฉพาะตัว ด้วยตัวรถที่แบ่งเป็น 2 ส่วน ได้แก่ ส่วนหน้าเป็นห้องสำหรับโดยสาร และส่วนหลังเป็นกระบะสำหรับบรรทุกของและสามารถเปิดท้ายได้ โดยพื้นที่โดยสารจะแบ่งเป็นแบบ 2 ที่นั่ง หรือ 4 ที่นั่ง และขนาดกระบะจะแปรผันตามขนาดห้องโดยสารเพื่อให้มีขนาดความยาวที่เหมาะสม รวมถึงมีตัวเลือกขับเคลื่อน 2 ล้อหลัง และ 4 ล้อ สำหรับออฟโรด โดยรถประเภทนี้สามารถใช้งานได้ตั้งแต่เป็นรถยนต์นั่งทั่วไป จนถึงรถบรรทุกใช้งาน ซึ่งจะเป็นรถที่ได้รับความนิยมเป็นอย่างมากในตลาดเมืองไทย เพราะถือว่าเป็นประเทศที่ผลิตรถยนต์ประเภทนี้มากเป็นอันดับต้น ๆ ของโลก ซึ่งรถกระบะในบ้านเรานั้นจะมีให้เลือกด้วยกันหลายแบรนด์ อาทิ Toyota Hilux Revo, Isuzu D-Max, Mitsubishi Triton, Nissan Navara, Ford Ranger, Mazda BT-50 และค่ายรถยนต์จากเมืองจีนอย่าง MG Extender')
        st.subheader('8. รถมินิเอ็มพีวี (Mini MPV)')
        st.markdown('รถมินิเอ็มพีวี (Mini MPV) โดยคำว่า MPV ย่อมาจากคำว่า Multi Purpose Van เป็นรถอเนกประสงค์แบบ 5-7 ที่นั่ง จัดเป็นรถครอบครัวขนาดใหญ่ที่ออกแบบให้สามารถรองรับผู้โดยสารได้จำนวนมาก อีกทั้งยังมีพื้นที่เก็บสัมภาระด้านท้ายขนาดใหญ่ สำหรับรถ Mini MPV ที่ได้รับความนิยมก็มีหลายค่ายด้วยกัน ไม่ว่าจะเป็นรถ Honda BR-V, Mitsubishi Xpander, Toyota Avanza หรือล่าสุดถูกเปลี่ยนชื่อมาเป็น Toyota Veloz และ Suzuki XL7')
        st.subheader('9. รถแวน (Van)')
        st.markdown('รถแวน (Van) รถประเภทนี้จะมีจุดเด่นที่หลังคาสูงใหญ่ และเพื่อความสะดวกสบายในขณะเข้า-ออก จึงต้องมาพร้อมกับประตูสไลด์ ส่วนภายในจะสามารถปรับตำแหน่งเบาะนั่งได้ด้วยรางบนพื้น และไม่มีเนินครอบเพลากลางเนื่องจากตัวรถยกสูง ทำให้เข้า-ออกได้คล่องตัว เป็นรถที่ออกแบบมาสำหรับครอบครัวโดยเฉพาะ และมีหลายขนาดเพื่อรองรับการใช้งานที่หลากหลาย โดยรถในกลุ่มนี้ในตลาดเมืองไทยก็จะมี Hyundai Staria, Toyota Hiace และ Volkswagen Caravelle เป็นต้น')
        st.subheader('10. รถเปิดประทุน (Cabrio)')
        st.markdown('รถเปิดประทุน หรือเรียกอีกอย่างว่า รถ Convertible เป็นรถยนต์สปอร์ต 2 ประตู ที่มีขนาดทั้งเล็ก กลาง และใหญ่ ให้เลือกใช้งาน มีจำนวนที่นั่งจำกัดแค่เพียง 2-4 ที่นั่ง ขึ้นอยู่กับแต่ละรุ่นหรือแบรนด์ เรตราคาก็มีให้เลือกตั้งแต่ล้านต้น ๆ ไปจนถึงหลักสิบล้านบาท แต่ความพิเศษอย่างหนึ่งที่ทำให้รถเปิดประทุนมีความน่าสนใจและแตกต่างจากรถชนิดอื่น ๆ ก็คือ หลังคาที่สามารถเปิด-ปิดได้ ตรงจุดนี้นี่เองที่ช่วยเพิ่มสุนทรียภาพในการขับขี่ ช่วยให้การเดินทางโดยเฉพาะวันที่อากาศดี ๆ ท่องเที่ยวริมทะเล หรือภูเขา ฟินมากยิ่งขึ้นไปอีก โดยในรุ่นที่น่าสนใจจะมีทั้ง BMW Z4 Roadster M40i และ Mercedes Benz SL Roadsterนอกากนี้ยังมีรถเปิดประทุนที่ถูกเรียกว่า Roadster หรือ Spyder จุดเด่นของรถประเภทนี้คือ เป็นรถที่ไม่มีหลังคา หรือเป็นหลังคาแข็งแบบหลังคาแก้วหรือ Targa ที่สามารถยกหรือถอดออกได้ โดยรุ่นที่คุ้นตาสำหรับรถประเภทก็จะเป็น Audi TT Roadster และ Aston Martin Vantage Roadster ประเภทของรถยนต์')
        st.subheader('11. สปอร์ตคาร์ (Sportcar)')
        st.markdown('สำหบรถกลุ่มนี้จะต่อยอดมาจากตัวถังคูเป้เป็นหลัก แต่มีบางรุ่นที่เป็นแบบ 4 ประตู โดยเน้นการออกแบบให้ลู่ลมมากที่สุด เกาะถนนมากที่สุด มาพร้อมกับเครื่องยนต์กำลังสูง ทั้งการออกแบบให้มีความสูงใต้ท้องรถที่ต่ำ ล้อขนาดใหญ่ และส่วนมากเครื่องยนต์จะวางกลางหรือวางหลัง ไปจนถึงการใช้วัสดุน้ำหนักเบามาประกอบตัวถัง นอกจากนี้ในประเภทสปอร์ตคาร์ยังถูกแบ่งแยกย่อยออกตามพละกำลังของเครื่องยนต์ รวมถึงรูปลักษณ์ โดยจะแบ่งและเรียกชื่อแตกต่างกัน ดังนี้ ซูเปอร์คาร์ (Supercar) เป็นรถที่มีสมรรถนะมากกว่า 500 แรงม้าขึ้นไป อาทิ Porsche 911, Mercedes Amg GT, Lamborghini Huracan และ Ferrari 488 เป็นต้นมัสเซิลคาร์ (Muscle Car) ที่เน้นเครื่องยนต์ทรงพลัง พร้อมตัวถังที่บึกบึน โดดเด่น อาทิ Ford Mustang และ Dodge Challenger ไฮเปอร์คาร์ (Hypercar) ที่ใช้เทคโนโลยีจากรถแข่งมาใส่ไว้ในรถสปอร์ต เครื่องยนต์ที่ให้กำลังมากกว่า 800 ถึงพันแรงม้าขึ้นไป ภายใต้รูปทรงที่โฉบเฉี่ยว และที่สำคัญคือมักผลิตในจำนวนจำกัด แถมราคาตีเลขไทยทะลุร้อยล้าน อาทิ Bugatti Veyron, Pagani Huayra, Ferrari LaFerrari และ McLaren P1ประเภทของรถยนต์')
        st.markdown('https://car.kapook.com/view253221.html')