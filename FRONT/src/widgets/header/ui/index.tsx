import React, { useState } from 'react';
import Logo from '../../../app/assets/photos/Logo_SHD.png';
import '../../../app/styles/header/header.css';
import ActiveRightHand from '../../../app/assets/photos/Hands/Right_Active.png';
import InactiveRightHand from '../../../app/assets/photos/Hands/Right_Inactive.png';
import ActiveLeftHand from '../../../app/assets/photos/Hands/Left_Active.png';
import InactiveLeftHand from '../../../app/assets/photos/Hands/Left_Inactive.png';

function Header() {
  const [isRightHandActive, setIsRightHandActive] = useState(false);
  const [isLeftHandActive, setIsLeftHandActive] = useState(true);

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
    </div>
  );
}

export default Header;