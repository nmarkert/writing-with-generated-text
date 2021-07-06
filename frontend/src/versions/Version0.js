import TextField from '../js_components/TextField'
import Baseline from './Baseline'

class Version0 extends Baseline {

    render() {
        return(
            <>
            <div>
                <TextField 
                    stop={() => {}}
                    on_submit={() => {}} 
                    sentence={this.state.sentence} 
                    handle_typing={this.handle_typing}
                    disabled={false}
                />
            </div>
            </>
        );
    }
}

export default Version0;