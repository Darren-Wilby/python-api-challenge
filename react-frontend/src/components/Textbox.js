import React from 'react';
import { Input } from 'semantic-ui-react';

const Textbox = ({ placeholder, value, onChange }) => (
    <Input size="large" type="text" placeholder={placeholder} value={value} onChange={onChange} />
);

export default Textbox;