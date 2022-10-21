import back_arrow from "../../assets/arrow-left.svg"
import './BackArrow.css'

interface BackArrowProps {
    callback?: () => void
}

export const BackArrow = ({callback}: BackArrowProps) => (
    <img src={back_arrow} alt="Back Arrow" className="back-arrow" onClick={callback}/>
)