import React, { useRef } from 'react'
import { toPng } from 'html-to-image'
import Profile from '../Sample_Data/JonathanJones.jpeg'
import QR from '../Sample_Data/Jonathan_Jones_Full Stack Software Devoloper.jpg'

const Business_Card = () => {
    const elementRef = useRef(null);
    const htmlToImageConvert = () =>{
        toPng(elementRef.current,{cacheBust:false})
        .then((dataUrl) =>{
            const link = document.createElement("a");
            link.download = "Business_Card.png";
            link.href = dataUrl;
            link.click();
        })
        .catch((err)=>{
            console.log(err);
        })
    }
  return (
   <>
   <div
    ref={elementRef}
    style={{
        background: 'white',
        width:'640px'
    }}
    >
      <div id="card">
      <div id="foreground_img">
          <img id="profile" src={Profile} alt="Profile Picture" style={{
        background: 'white',
        width:'440px'
    }}/>
          <div id="text-position">
            <h2> First Name</h2>
            <h2> Last Name </h2>
            <h3> Role </h3>
          </div>
          <img
          id="qrcode"
            src={QR}
            alt="QR Code"
          />
      </div>
    </div>
    </div>
    <button onClick={htmlToImageConvert}>Download</button>
   </>
    
  )
}

export default Business_Card