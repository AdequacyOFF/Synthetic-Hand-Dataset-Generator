import React, {useState} from "react";
import Start_Generate from '../../../app/assets/photos/generateStart.svg'
import End_Generate from '../../../app/assets/photos/generateEnd.svg'
import '../../../app/styles/Generate/Generate.css'


const Generate: React.FC = () =>{

    const [isStartActive, setIsStartActive] = useState(true);
    const [isEndActive, setIsEndActive] = useState(false);

    const toggleStartState = () => {
        if (isStartActive)
        {
            setIsStartActive(false);
            setIsEndActive(true);
        }
        
      };
    
      const toggleEndState = () => {
        if (isEndActive)
        {
            setIsEndActive(false);
            setIsStartActive(true);
        }
       
      };

    return (
        <div className="Generate-wrapper">
            <img src={Start_Generate} alt="" className="Generate start" id ={isStartActive ? 'Active' : 'Inactive'} onClick={toggleStartState} />
            <img src={End_Generate} alt="" className="Generate end" id ={isEndActive ? 'Active' : 'Inactive'} onClick={toggleEndState} />
        </div>
    )
}

export default Generate;