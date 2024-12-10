# TxtTransTool
A tool to assist with ETRI dual-transcription rule text labeling tasks<br>

※ Ver2.0 Latest Update Date 2020.12.21<br>
※ For any inquiries, contact sjy777star@gmail.com.<br>

<How To Use>
※ The 'Dual Transcription Tool' is a self-developed program, and security pop-ups from Windows Defender may appear. Please disable Defender temporarily to use the tool. <br>
※ Enter the text you want to transcribe and press Enter or Enter (Convert) to proceed with the transcription.<br>
※ After extracting the folder, you can use the TxtTransTool-Shortcut program within the folder,<br>
or right-click on TxtTransTool.exe to create a shortcut directly within the folder and place it on the desktop or another convenient location for use.<br>
<br>
  
## Function
<Ver2.0 Update Function>
* Number Transcription: Expanded number handling to include up to billions, decimals, and numbers with trailing zeros.
    - ex. (12345672.124)/(천 이백 삼십 사만 오천 육백 칠십 이 점 일 이 사)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102712558-83333200-4305-11eb-9d01-95867ad7cba6.png)<br>

* Alphabet Pronunciation Transcription: Preserves existing Ver1.0 functionality.
  - ex. (EBS)/(이 비 에스)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102716823-9d7b0900-4321-11eb-92fb-c53282651f71.png)<br>

* Korean Consonant Transcription: Supports transcription of consonants (ㄱ-ㅎ) to their full phonetic forms. 
  - ex. (ㄱ)/(기역)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102716850-ca2f2080-4321-11eb-99e2-8a1a493b9ee6.png)<br>
  
* Mixed Korean and Number Transcriptions: Handles combinations of Korean and numbers.
  - ex. (1948년)/(천 구백 사십 팔 년)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102718052-6872b480-4329-11eb-9cae-7f413ec7e6f5.png)<br>
  
* Mixed Alphabet and Number Transcriptions: Handles combinations of English alphabet and numbers.
  - ex. (C16)/(씨 십 육)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102718696-d1a7f700-432c-11eb-89c1-5709d9da8a5d.png)<br>
  
* Korean, Alphabet, and Number Combination Transcription:
  - ex. (3x명)/(삼 엑스 명)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102718688-c0f78100-432c-11eb-9d78-ab142d155ae7.png)<br>
  
* Flexible Number Pronunciation: For integers within 0-99, multiple pronunciation outputs are provided for context-specific use.
  - ex. (H2O)/(에이치 이 오)
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(H2O)/(에이치 투 오) --> Select
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(H2O)/(에이치 두 오) 
  - ex. (4C2)/(사 씨 이) --> 선택 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(4C2)/(포 씨 투) 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(4C2)/(네 씨 두) 
  - ex. (9개)/(구 개) 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(9개)/(나인 개) 
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(9개)/(아홉 개) --> Select <br>
  ![image](https://user-images.githubusercontent.com/46860669/102718153-f9499000-4329-11eb-9b0c-dd82829f3d19.png)<br>

 * Date Handling: Transcribes dates differentiating to floating-point numbers:
   - ex. (10.26)/(십 이 육) <-- Output as a date
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(10.26)/(십 점 이 육) <-- Output as a floating-point number<br>
   ![image](https://user-images.githubusercontent.com/46860669/102718205-46c5fd00-432a-11eb-8f3a-b0585f0ca660.png)<br>
        
 * Colloquial Speech Standardization: Converts colloquial expressions into standard forms.
   - ex. (그렇죠)/(그쵸)<br>
  ![image](https://user-images.githubusercontent.com/46860669/102710691-68f25780-42f7-11eb-95fb-e4d4def2cb6d.png)<br>
  
 * Korean-English Transcription: Provides English pronunciations or translations for Korean inputs.
    - ex. (cloud)/(클라우드) <br>
  ![한영전사](https://user-images.githubusercontent.com/46860669/102710567-7529e500-42f6-11eb-9e8f-4e284e6018aa.PNG)<br>
  
 * Full Sentence Dual Transcription: Allows dual transcription for entire sentences. Add quotation marks around the target text and end with a semicolon (;) to use this function.
    - ex. 자/ 일단 '요기;' 한 번 볼게요. 'ㄱ;' 은 뭐죠? '그죠;'. '3.45x;'! 맞나요? '굿;'입니다. 자/ 'ㄴ;' 봐볼까요? 이건 '플러스;' '3 분의 1;'이네요. 
  <br>--> 자/ 일단 (여기)/(요기) 한 번 볼게요. (ㄱ)/(기역) 은 뭐죠? (그렇죠)/(그죠). (3.45x)/(삼 점 사 오 엑스)! 맞나요? (good)/(굿)입니다. 자/ (ㄴ)/(니은) 봐볼까요? 이건 (plus)/(플러스) (3 분의 1)/(삼 분의 일) 이네요.<br>
![image](https://user-images.githubusercontent.com/46860669/102718631-7bd34f00-432c-11eb-9bab-1d16e82577a7.png)<br>

* Additional Features:
    - Use the Windows key + arrow keys to move windows.
    - Adjust window height as needed.
<br><br>
------------------------------------------------------------------------------------<br>
* Project Start Date: Dec.15, 2020 <br>
* Dec.17, 2020: <br>
  - Completed integer and decimal processing (up to billions).
  - Finalized alphabet transcription handling.
  - Mixed alphabet and number transcription implemented.
  - Enhanced English/Korean pronunciation outputs for 0-99.
  - Enabled full-sentence transcription with quotation marks.
  - English pronunciation or translation functionality for Korean inputs.
    * ex. (cloud)/(클라우드)
<br><br>
* Dec.20, 2020 Update:
  - Fixed spacing issues in Korean processing.
    * ex. (24시간)/(이십 사 시 간)  --> (24시간)/(이십 사 시간)
  - Allowed spaces within the input text.
    * ex. (4 분의 1)/(사 분의 일)
