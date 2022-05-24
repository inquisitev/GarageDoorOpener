import { Button } from "antd"

const DoorControlsComponent = (props) => {
    return <div>
        <p>DoorState: {props.doorState}</p>
        <button onClick={props.getDoorState}>Update Door State</button>
        <button onClick={props.doorTrigger}>Trigger Door</button>
    </div>
}

export default DoorControlsComponent