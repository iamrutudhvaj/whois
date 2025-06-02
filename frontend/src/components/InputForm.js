import React, { useState } from 'react';

function InputForm({ onSubmit }) {
    const [domainName, setDomainName] = useState('');
    const [dataType, setDataType] = useState('domain');

    const handleSubmit = (e) => {
        e.preventDefault();
        onSubmit({ domainName, dataType });
    };

    return (
        <form onSubmit={handleSubmit} className="mb-6 p-6 bg-white rounded shadow-md">
            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="domainName">
                    Domain Name
                </label>
                <input
                    id="domainName"
                    type="text"
                    placeholder="Enter a domain (e.g., amazon.com)"
                    value={domainName}
                    onChange={(e) => setDomainName(e.target.value)}
                    className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
                    required
                />
            </div>

            <div className="mb-4">
                <label className="block text-gray-700 text-sm font-bold mb-2">
                    Information Type
                </label>
                <div className="mt-2">
                    <label className="inline-flex items-center mr-4">
                        <input
                            type="radio"
                            value="domain"
                            checked={dataType === 'domain'}
                            onChange={() => setDataType('domain')}
                            className="form-radio h-5 w-5 text-blue-600"
                        />
                        <span className="ml-2 text-gray-700">Domain Information</span>
                    </label>
                    <label className="inline-flex items-center">
                        <input
                            type="radio"
                            value="contact"
                            checked={dataType === 'contact'}
                            onChange={() => setDataType('contact')}
                            className="form-radio h-5 w-5 text-blue-600"
                        />
                        <span className="ml-2 text-gray-700">Contact Information</span>
                    </label>
                </div>
            </div>

            <div className="flex items-center justify-center">
                <button
                    type="submit"
                    className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
                >
                    Look Up Domain
                </button>
            </div>
        </form>
    );
}

export default InputForm;