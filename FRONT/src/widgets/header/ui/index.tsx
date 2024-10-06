import React, { useState } from 'react';
import Logo from '../../../app/assets/photos/Logo_SHD.png';
import '../../../app/styles/header/header.css';
import ActiveRightHand from '../../../app/assets/photos/Hands/Right_Active.png';
import InactiveRightHand from '../../../app/assets/photos/Hands/Right_Inactive.png';
import ActiveLeftHand from '../../../app/assets/photos/Hands/Left_Active.png';
import InactiveLeftHand from '../../../app/assets/photos/Hands/Left_Inactive.png';
import LogoAD from '../../../app/assets/photos/Logo_ADOff.png'

function Header() {
  const [isRightHandActive, setIsRightHandActive] = useState(false);
  const [isLeftHandActive, setIsLeftHandActive] = useState(true);
  const [isDarkActive, setIsDarkActive] = useState(false);
  const [isLightActive, setIsLightActive] = useState(true);

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
      <div className='ADOff'>
        <img src={LogoAD} alt="" />
        <p>AdequacyOFF</p>
      </div>
    </div>
  );
}

export default Header;