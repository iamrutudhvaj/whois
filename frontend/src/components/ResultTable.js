import React from 'react';

function ResultTable({ data, type }) {
    const renderTableContent = () => {
        if (type === 'domain') {
            return (
                <>
                    <tr>
                        <td className="font-semibold">Domain Name</td>
                        <td>{data['Domain Name']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Registrar</td>
                        <td>{data['Registrar']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Registration Date</td>
                        <td>{data['Registration Date']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Expiration Date</td>
                        <td>{data['Expiration Date']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Estimated Domain Age</td>
                        <td>{data['Estimated Domain Age']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Hostnames</td>
                        <td>{data['Hostnames']}</td>
                    </tr>
                </>
            );
        } else if (type === 'contact') {
            return (
                <>
                    <tr>
                        <td className="font-semibold">Registrant Name</td>
                        <td>{data['Registrant Name']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Technical Contact Name</td>
                        <td>{data['Technical Contact Name']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Administrative Contact Name</td>
                        <td>{data['Administrative Contact Name']}</td>
                    </tr>
                    <tr>
                        <td className="font-semibold">Contact Email</td>
                        <td>{data['Contact Email']}</td>
                    </tr>
                </>
            );
        }

        return <tr><td colSpan="2">Unknown data type</td></tr>;
    };

    return (
        <div className="mt-6 p-6 bg-white rounded shadow-md">
            <h2 className="text-xl font-semibold mb-4">
                {type === 'domain' ? 'Domain Information' : 'Contact Information'}
            </h2>
            <div className="overflow-x-auto">
                <table className="min-w-full bg-white">
                    <tbody className="divide-y divide-gray-200">
                        {renderTableContent()}
                    </tbody>
                </table>
            </div>
        </div>
    );
}

export default ResultTable;