import { Button } from "antd"

export default  doorControls = (props) => {
    return <div>
        <p>DoorState: {props.doorState}</p>
        <Button onClick={props.doorTrigger}/>
    </div>
}