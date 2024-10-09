import  React, { useState } from 'react';
import Logo from '../../../app/assets/photos/Logo_SHD.png';
import '../../../app/styles/header/header.css';
import ActiveRightHand from '../../../app/assets/photos/Hands/Right_Active.png';
import InactiveRightHand from '../../../app/assets/photos/Hands/Right_Inactive.png';
import ActiveLeftHand from '../../../app/assets/photos/Hands/Left_Active.png';
import InactiveLeftHand from '../../../app/assets/photos/Hands/Left_Inactive.png';
import LogoAD from '../../../app/assets/photos/Logo_ADOff.png'
import Start_Generate from '../../../app/assets/photos/generateStart.svg'
import End_Generate from '../../../app/assets/photos/generateEnd.svg'
import Loading from '../../../app/assets/videos/hend_3.gif'


const Header:React.FC = () =>{
  const [isRightHandActive, setIsRightHandActive] = useState(false);
  const [isLeftHandActive, setIsLeftHandActive] = useState(true);
  const [isDarkActive, setIsDarkActive] = useState(false);
  const [isLightActive, setIsLightActive] = useState(true);
  const [isStartActive, setIsStartActive] = useState(true);
  const [isEndActive, setIsEndActive] = useState(false);
  const [inputValue, setInputValue] = useState('');
  const [isLinkResive, setIsLinkResive] = useState(false);

  

  const handSide = () =>
  {
    if (isRightHandActive)
    {
      return "Right";
    }
    else
    {
      return "Left";
    }
  }
  const race = () =>
    {
      if (isDarkActive)
      {
        return "Dark";
      }
      else
      {
        return "Light";
      }
    }


  const toggleRightHandState = () => {
    if (!isRightHandActive)
    {
        setIsRightHandActive(true);
        setIsLeftHandActive(false);
    }
    
  };

  const toggleLeftHandState = () => {
    if (!isLeftHandActive)
    {
        setIsRightHandActive(false);
        setIsLeftHandActive(true);
    }
   
  };

  const toggleLightState = () => {
    if (!isLightActive)
    {
        setIsLightActive(true);
        setIsDarkActive(false);
    }
    
  };

  const toggleDarkState = () => {
    if (!isDarkActive)
    {
        setIsLightActive(false);
        setIsDarkActive(true);
    }
   
  };

  const toggleStartState = () => {
    if (isStartActive && inputValue !== '')
    {
        setIsStartActive(false);
        setIsEndActive(true);
        setInputValue('')
        fetch('http://localhost:5020/generate-hand-dataset', {
          method: 'POST', // or 'PUT'
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            count: inputValue,
            race: race(),
            hand: handSide(),
          }),
        })
        .then(response => {
          if (response.ok) {
            return response.blob();
          } else {
            throw new Error('Failed to fetch file');
          }
        })
        .then(blob => {
          // Handle the file blob here
          const file = new File([blob], 'GeneratedHand-archive.zip', { type: blob.type });
          // You can now use the `file` object for further processing or saving it to the client
          console.log('File:', file);
          const url = URL.createObjectURL(file);
          const link = document.createElement('a');
          link.href = url;
          link.download = 'GeneratedHand-archive.zip'; // Replace 'GeneratedHand-archive.zip' with the desired file name
          link.click();
          setIsLinkResive(true);
        })
        .catch((error) => {
          console.error('Error:', error);
        });
    }
    
  };

  const toggleEndState = () => {
    if (isEndActive && isLinkResive)
    {
        setIsEndActive(false);
        setIsStartActive(true);
        setIsLinkResive(false);
    }
  }; 
  const handleInputChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setInputValue(event.target.value);
  };
  
  const handleFormSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    console.log(inputValue)
    event.preventDefault();
    setInputValue(''); 
   
  };



  return (
    <div className="wrapper-header">
      <div className="logo_SHD"> <img src={Logo} alt="" /> </div>
      <div className='Hand'>
      
      <div className="left" >
        <img
          src={isLeftHandActive ? ActiveLeftHand : InactiveLeftHand}
          alt="Left Hand"
          onClick={toggleLeftHandState}
        />
      </div>
      <div className='right' >
        <img
          src={isRightHandActive ? ActiveRightHand : InactiveRightHand}
          alt="Right Hand"
          onClick={toggleRightHandState}
        />
      </div>
      </div>
      <div className='Change-Skin'>
        <p className='Skin'>КОЖА</p>
        <p className='Light'><button className={isLightActive ? 'Active' : 'Inactive'} onClick={toggleLightState}>СВЕТЛАЯ</button></p>
        <p className='Dark'><button className={isDarkActive ? 'Active' : 'Inactive'} onClick={toggleDarkState}>ТЁМНАЯ</button></p>
      </div>
      <div className='Count'>
        <p>КОЛИЧЕСТВО</p>
        <form onSubmit={handleFormSubmit}>
          <input type="number" max={10000} min={1} inputMode="numeric" value={inputValue} onChange={handleInputChange} />
        </form>
      </div>
      <div className='ADOff'>
        <img src={LogoAD} alt="" />
        <p>AdequacyOFF</p>
      </div>
      <div className="Generate-wrapper">
            <img src={Start_Generate} alt="" className="Generate start" id ={isStartActive ? 'Active' : 'Inactive'} onClick={toggleStartState} />
            <img src={End_Generate} alt="" className="Generate end" id ={isEndActive ? 'Active' : 'Inactive'} onClick={toggleEndState} />
            <img src={Loading} alt="video/gif" className='Loading_gif'id ={isEndActive && !isLinkResive  ? 'Active' : 'Inactive'}/>
        </div>
    </div>
  );
}

export default Header;